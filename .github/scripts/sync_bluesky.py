import os
import re
from datetime import datetime, timezone

import requests
from atproto import Client

# --- Configuration ---
HANDLE = os.getenv("BLUESKY_HANDLE")
APP_PASSWORD = os.getenv("BLUESKY_PASSWORD")
OUTPUT_DIR = "_posts"
IMAGE_DIR = "assets/images/microblog"
SITE_IMAGE_PATH = "/assets/images/microblog"
LAST_RUN_FILE = ".last_run_timestamp"

# --- Setup ---
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)

client = Client()
client.login(HANDLE, APP_PASSWORD)


# --- Helper Functions ---
def slugify(text, limit=30):
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text[:limit] or "untitled"


def download_image(url, slug, index):
    ext = os.path.splitext(url.split("?")[0])[1] or ".jpg"
    if not ext.startswith("."):
        ext = "." + ext
    filename = f"{slug}-{index}{ext}"
    filepath = os.path.join(IMAGE_DIR, filename)
    try:
        resp = requests.get(url, stream=True)
        resp.raise_for_status()
        with open(filepath, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        return f"{SITE_IMAGE_PATH}/{filename}"
    except requests.RequestException as e:
        print(f"  - Error downloading image {url}: {e}")
        return None


def get_last_run_timestamp():
    if not os.path.exists(LAST_RUN_FILE):
        return None
    with open(LAST_RUN_FILE, "r") as f:
        try:
            return datetime.fromisoformat(f.read().strip())
        except (ValueError, TypeError):
            return None


def save_last_run_timestamp(timestamp):
    with open(LAST_RUN_FILE, "w") as f:
        f.write(timestamp.isoformat())


# --- Main Logic ---
print("Starting Bluesky sync...")
last_run_ts = get_last_run_timestamp()

if last_run_ts:
    print(f"Fetching posts created after: {last_run_ts.strftime('%Y-%m-%d %H:%M:%S')}")
else:
    print("No previous run timestamp found. Fetching all posts.")

feed = client.app.bsky.feed.get_author_feed({"actor": HANDLE, "limit": 100})

root_posts = []
for item in feed.feed:
    is_root_post = not (
        hasattr(item.post.record, "reply") and item.post.record.reply is not None
    )
    if is_root_post:
        post_ts = datetime.fromisoformat(
            item.post.record.created_at.replace("Z", "+00:00")
        ).astimezone(timezone.utc)
        if not last_run_ts or post_ts > last_run_ts.astimezone(timezone.utc):
            root_posts.append(item)

if not root_posts:
    print("No new posts to sync.")
    exit()

print(f"Found {len(root_posts)} new posts to process.")
root_posts.sort(
    key=lambda x: datetime.fromisoformat(
        x.post.record.created_at.replace("Z", "+00:00")
    )
)

for i, item in enumerate(root_posts):
    post_record = item.post.record
    timestamp = datetime.fromisoformat(post_record.created_at.replace("Z", "+00:00"))
    first_line_of_text = (
        post_record.text.split("\n")[0] if post_record.text.strip() else ""
    )
    slug = slugify(first_line_of_text, limit=30)
    filename = f"{timestamp.strftime('%Y-%m-%d')}-{slug}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    title_line = f"\U0001f535\u2601\ufe0f # {i + 1:03d}"

    print(f"Processing post: {filename}")

    all_text_blocks = []
    all_image_paths = []

    thread_view = client.app.bsky.feed.get_post_thread(
        {"uri": item.post.uri, "depth": 100}
    )

    def process_thread_node(node, counter):
        if node.post.author.handle != HANDLE:
            return counter

        current_post_text_block = []
        ts = datetime.fromisoformat(node.post.record.created_at.replace("Z", "+00:00"))
        current_post_text_block.append(f"**{ts.strftime('%B %d, %Y at %I:%M %p')}**")

        text_content = node.post.record.text.strip()
        if text_content:
            current_post_text_block.append(text_content)

        all_text_blocks.append("\n\n".join(current_post_text_block))

        images_in_node = (
            node.post.embed.images if hasattr(node.post.embed, "images") else []
        )
        for img in images_in_node:
            img_url = img.fullsize
            local_path = download_image(img_url, slug, counter)
            if local_path:
                all_image_paths.append(local_path)
                counter += 1

        if hasattr(node, "replies") and node.replies:
            for reply in sorted(node.replies, key=lambda r: r.post.record.created_at):
                counter = process_thread_node(reply, counter)
        return counter

    if thread_view.thread:
        process_thread_node(thread_view.thread, 0)

    front_matter_images_str = ""
    post_content = "\n\n---\n\n".join(all_text_blocks)

    if len(all_image_paths) > 1:
        image_list_yaml = "\n".join([f"  - {p}" for p in all_image_paths])
        front_matter_images_str = f"images:\n{image_list_yaml}"
    elif len(all_image_paths) == 1:
        alt_text = slugify(first_line_of_text) or "Post image"
        image_md = f"![{alt_text}]({all_image_paths[0]}){{: .blog-image .med}}\n\n"
        post_content = image_md + post_content

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write("layout: microblog_post\n")
        f.write(f'title: "{title_line}"\n')
        f.write(f"date: {timestamp.strftime('%Y-%m-%d %H:%M:%S %z')}\n")
        if front_matter_images_str:
            f.write(front_matter_images_str)
        f.write("---\n\n")
        f.write(post_content)

    print(f"  -> Created file: {filepath}")

if root_posts:
    latest_post_ts = datetime.fromisoformat(
        root_posts[-1].post.record.created_at.replace("Z", "+00:00")
    )
    save_last_run_timestamp(latest_post_ts)
    print(
        f"\nSync complete. Last run timestamp updated to: {latest_post_ts.isoformat()}"
    )
