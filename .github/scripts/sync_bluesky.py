import os
import re
from datetime import datetime
from zoneinfo import ZoneInfo  # Use the modern, built-in timezone library

import requests
from atproto import Client
from PIL import Image

# --- Configuration ---
HANDLE = os.getenv("BLUESKY_HANDLE")
APP_PASSWORD = os.getenv("BLUESKY_PASSWORD")
OUTPUT_DIR = "_posts"
IMAGE_DIR = "assets/images/microblog"
SITE_IMAGE_PATH = "/assets/images/microblog"
LAST_RUN_FILE = ".last_run_timestamp"
MAX_LONG_EDGE = 2048
TIMEZONE = "America/New_York"  # Define the target timezone

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


def get_image_dimensions(filepath):
    try:
        with Image.open(filepath) as img:
            return img.size
    except Exception as e:
        print(f"  - Could not get dimensions for {filepath}: {e}")
        return (0, 0)


def process_and_convert_image(input_path):
    try:
        img = Image.open(input_path)

        long_edge = max(img.size)
        if long_edge > MAX_LONG_EDGE:
            aspect_ratio = img.width / img.height
            if img.width > img.height:
                new_size = (MAX_LONG_EDGE, int(MAX_LONG_EDGE / aspect_ratio))
            else:
                new_size = (int(MAX_LONG_EDGE * aspect_ratio), MAX_LONG_EDGE)
            img = img.resize(new_size, Image.Resampling.LANCZOS)

        webp_path = os.path.splitext(input_path)[0] + ".webp"
        img.save(webp_path, "webp", quality=85)

        if os.path.splitext(input_path)[1].lower() != ".webp":
            os.remove(input_path)

        return webp_path

    except Exception as e:
        print(f"  - Error processing image {input_path}: {e}")
        return None


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

        processed_path = process_and_convert_image(filepath)
        if processed_path:
            new_web_path = f"{SITE_IMAGE_PATH}/{os.path.basename(processed_path)}"
            return (new_web_path, processed_path)
        else:
            return (None, None)

    except requests.RequestException as e:
        print(f"  - Error downloading image {url}: {e}")
        return (None, None)


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
        # Timestamps from the API are in UTC
        post_ts_utc = datetime.fromisoformat(
            item.post.record.created_at.replace("Z", "+00:00")
        )
        if not last_run_ts or post_ts_utc > last_run_ts:
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

image_counter = 0

for i, item in enumerate(root_posts):
    post = item.post.record
    utc_timestamp = datetime.fromisoformat(post.created_at.replace("Z", "+00:00"))
    local_timestamp = utc_timestamp.astimezone(ZoneInfo(TIMEZONE))

    first_line_of_text = post.text.split("\n")[0] if post.text.strip() else ""
    slug = slugify(first_line_of_text, limit=30)
    filename = f"{local_timestamp.strftime('%Y-%m-%d')}-{slug}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    title_line = f"\U0001f535\u2601\ufe0f # {i + 1:03d}"

    print(f"Processing post: {filename}")

    all_images_for_frontmatter = []
    thread_parts = []

    thread_view = client.app.bsky.feed.get_post_thread(
        {"uri": item.post.uri, "depth": 100}
    )

    def process_node_recursively(node):
        global image_counter
        if node.post.author.handle != HANDLE:
            return

        part = {"text": node.post.record.text.strip(), "images": [], "timestamp": None}
        part["timestamp"] = datetime.fromisoformat(
            node.post.record.created_at.replace("Z", "+00:00")
        )

        images_in_node = (
            node.post.embed.images if hasattr(node.post.embed, "images") else []
        )
        for img in images_in_node:
            img_url = img.fullsize
            web_path, local_fs_path = download_image(img_url, slug, image_counter)
            if web_path and local_fs_path:
                all_images_for_frontmatter.append(web_path)
                width, height = get_image_dimensions(local_fs_path)
                alt_text = img.alt or "Thread image"
                html_tag = f'<a href="{web_path}" class="photoswipe" data-pswp-width="{width}" data-pswp-height="{height}" target="_blank" rel="noopener noreferrer"><img src="{web_path}" alt="{alt_text}" loading="lazy"></a>'
                part["images"].append(html_tag)
                image_counter += 1

        thread_parts.append(part)

        if hasattr(node, "replies") and node.replies:
            for reply in sorted(node.replies, key=lambda r: r.post.record.created_at):
                process_node_recursively(reply)

    if thread_view.thread:
        process_node_recursively(thread_view.thread)

    final_content_parts = []
    if thread_parts:
        root_part = thread_parts[0]
        if root_part["text"]:
            final_content_parts.append(root_part["text"])

        if root_part["images"] or len(thread_parts) > 1:
            final_content_parts.append("\n\n\n\n")

        if root_part["images"]:
            final_content_parts.extend(root_part["images"])

        for reply_part in thread_parts[1:]:
            final_content_parts.append("\n---\n")
            # Convert timestamp to local timezone (EST/EDT)
            reply_ts_utc = reply_part["timestamp"]
            reply_ts_local = reply_ts_utc.astimezone(ZoneInfo(TIMEZONE))
            ts_str = f"**{reply_ts_local.strftime('%B %d, %Y at %I:%M %p')}**\n"
            final_content_parts.append(ts_str)
            if reply_part["text"]:
                final_content_parts.append(reply_part["text"])
            if reply_part["images"]:
                final_content_parts.extend(reply_part["images"])

    final_content = "\n".join(final_content_parts)

    front_matter_images_str = ""
    if all_images_for_frontmatter:
        image_list_yaml = "\n".join([f"  - {p}" for p in all_images_for_frontmatter])
        front_matter_images_str = f"images:\n{image_list_yaml}"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write("layout: microblog_post\n")
        f.write(f'title: "{title_line}"\n')
        f.write(
            f"date: {utc_timestamp.strftime('%Y-%m-%d %H:%M:%S %z')}\n"
        )  # Front matter date should remain UTC
        if front_matter_images_str:
            f.write(f"{front_matter_images_str}\n")
        f.write("---\n\n")
        f.write(final_content)

    print(f"  -> Created file: {filepath}")

if root_posts:
    # Save the timestamp of the last processed post in UTC
    latest_post_utc = datetime.fromisoformat(
        root_posts[-1].post.record.created_at.replace("Z", "+00:00")
    )
    save_last_run_timestamp(latest_post_utc)
    print(
        f"\nSync complete. Last run timestamp updated to: {latest_post_utc.isoformat()}"
    )
