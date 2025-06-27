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
LAST_RUN_FILE = ".last_run_timestamp"  # Stores the timestamp of the last run

# --- Setup ---
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)

client = Client()
client.login(HANDLE, APP_PASSWORD)


# --- Helper Functions from your original script ---
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
    resp = requests.get(url)
    if resp.ok:
        with open(filepath, "wb") as f:
            f.write(resp.content)
        return f"{SITE_IMAGE_PATH}/{filename}"
    return None


# --- New Helper Functions for Incremental Sync ---
def get_last_run_timestamp():
    """Reads the timestamp from the last run file."""
    if not os.path.exists(LAST_RUN_FILE):
        return None
    with open(LAST_RUN_FILE, "r") as f:
        try:
            return datetime.fromisoformat(f.read().strip())
        except (ValueError, TypeError):
            return None


def save_last_run_timestamp(timestamp):
    """Saves the timestamp to the last run file."""
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

# Filter for root posts that are new since the last run
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

# Sort posts by time ascending to process them in order and preserve your original title indexing
root_posts.sort(
    key=lambda x: datetime.fromisoformat(
        x.post.record.created_at.replace("Z", "+00:00")
    )
)

for i, item in enumerate(root_posts):
    post = item.post.record
    timestamp = datetime.fromisoformat(post.created_at.replace("Z", "+00:00"))

    # Use your original slugify logic
    first_line_of_text = post.text.split("\n")[0] if post.text.strip() else ""
    slug = slugify(first_line_of_text, limit=30)
    filename = f"{timestamp.strftime('%Y-%m-%d')}-{slug}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    # Preserve your original title format
    title_line = f"\U0001f535\u2601\ufe0f # {i + 1:03d}"

    # --- New Image and Content Logic ---
    front_matter_images_str = ""
    content_lines = []
    all_images_in_post = []

    thread = client.app.bsky.feed.get_post_thread({"uri": item.post.uri})
    is_thread = thread.thread.replies is not None and len(thread.thread.replies) > 0

    if is_thread:
        # Your original thread collection logic remains, we just handle images differently
        # NOTE: This assumes a thread's images are treated as a single collection for the post.
        temp_content = []

        # A modified version of your walk function to collect images and text separately
        def walk_and_collect(node, slug):
            post_text_content = []
            post_image_paths = []
            if node.post.author.handle != HANDLE:
                return [], []

            ts = datetime.fromisoformat(
                node.post.record.created_at.replace("Z", "+00:00")
            )
            post_text_content.append(f"**{ts.strftime('%B %d, %Y at %I:%M %p')}**")

            images_in_node = (
                node.post.embed.images if hasattr(node.post.embed, "images") else []
            )
            for img in images_in_node:
                img_url = img.fullsize
                # Use a unique index for each image download
                local_path = download_image(
                    img_url, slug, len(all_images_in_post) + len(post_image_paths)
                )
                if local_path:
                    post_image_paths.append(local_path)

            content = node.post.record.text.strip()
            if content:
                post_text_content.append(f"\n{content}")

            # Recurse and handle replies
            replies = getattr(node, "replies", []) or []
            all_reply_text = []
            all_reply_images = []
            if replies:
                post_text_content.append("\n---\n")

            for reply in replies:
                reply_text, reply_images = walk_and_collect(reply, slug)
                all_reply_text.extend(reply_text)
                all_reply_images.extend(reply_images)

            # Combine current post content with replies
            full_text_so_far = post_text_content + all_reply_text
            full_images_so_far = post_image_paths + all_reply_images
            return full_text_so_far, full_images_so_far

        content_lines, all_images_in_post = walk_and_collect(thread.thread, slug)

    else:
        # Logic for a single, non-thread post
        images = item.post.embed.images if hasattr(item.post.embed, "images") else []
        for j, img in enumerate(images):
            img_url = img.fullsize
            local_path = download_image(img_url, slug, j)
            if local_path:
                all_images_in_post.append(local_path)

        text = post.text.strip()
        if text:
            content_lines.append(text)

    # --- Apply Conditional Image Logic ---
    if len(all_images_in_post) > 1:
        image_list_yaml = "\n".join([f"  - {p}" for p in all_images_in_post])
        front_matter_images_str = f"images:\n{image_list_yaml}"
    elif len(all_images_in_post) == 1:
        # If there's one image, add it to the top of the content
        alt_text = slugify(first_line_of_text) or "Post image"
        image_md = f"![{alt_text}]({all_images_in_post[0]}){{: .blog-image .med}}\n"
        content_lines.insert(0, image_md)

    # --- Write the file ---
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write("layout: microblog_post\n")
        f.write(f'title: "{title_line}"\n')
        f.write(f"date: {timestamp.strftime('%Y-%m-%d %H:%M:%S %z')}\n")
        if front_matter_images_str:
            f.write(f"{front_matter_images_str}\n")
        f.write("---\n\n")
        f.write(f"{chr(10).join(content_lines)}\n")

    print(f"  -> Created file: {filepath}")

# After successfully processing all new posts, update the timestamp
if root_posts:
    # Get the timestamp of the most recent post from this run to save
    latest_post_ts = datetime.fromisoformat(
        root_posts[-1].post.record.created_at.replace("Z", "+00:00")
    )
    save_last_run_timestamp(latest_post_ts)
    print(
        f"\nSync complete. Last run timestamp updated to: {latest_post_ts.isoformat()}"
    )
