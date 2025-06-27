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
LAST_RUN_FILE = ".last_run_timestamp"  # File to store the timestamp of the last run

# --- Setup ---
# Ensure output directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)

# Init client
client = Client()
client.login(HANDLE, APP_PASSWORD)


# --- Helper Functions ---
def get_last_run_timestamp():
    """Reads the timestamp from the last run file."""
    if not os.path.exists(LAST_RUN_FILE):
        return None
    with open(LAST_RUN_FILE, "r") as f:
        try:
            return datetime.fromisoformat(f.read().strip())
        except ValueError:
            return None


def save_last_run_timestamp(timestamp):
    """Saves the timestamp to the last run file."""
    with open(LAST_RUN_FILE, "w") as f:
        f.write(timestamp.isoformat())


def slugify(text, limit=30):
    """Generates a URL-friendly slug from text."""
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text[:limit] or "untitled"


def download_image(url, slug, index):
    """Downloads an image and returns its local path."""
    try:
        ext = os.path.splitext(url.split("?")[0])[1] or ".jpg"
        if not ext.startswith("."):
            ext = "." + ext
        filename = f"{slug}-{index}{ext}"
        filepath = os.path.join(IMAGE_DIR, filename)
        resp = requests.get(url, stream=True)
        resp.raise_for_status()
        with open(filepath, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        return f"{SITE_IMAGE_PATH}/{filename}"
    except requests.RequestException as e:
        print(f"Error downloading image {url}: {e}")
        return None


# --- Main Logic ---
print("Starting Bluesky sync...")

# Get the timestamp from the last successful run
last_run_ts = get_last_run_timestamp()
if last_run_ts:
    print(f"Fetching posts created after: {last_run_ts}")
else:
    print("No previous run timestamp found. Fetching all posts.")

feed = client.app.bsky.feed.get_author_feed({"actor": HANDLE, "limit": 100})

# Filter for root posts that are new since the last run
new_root_posts = []
for item in feed.feed:
    # A post is a root post if it's not a reply
    is_root_post = not (
        hasattr(item.post.record, "reply") and item.post.record.reply is not None
    )
    if is_root_post:
        post_ts = datetime.fromisoformat(
            item.post.record.created_at.replace("Z", "+00:00")
        ).astimezone(timezone.utc)
        # Process post only if it's newer than the last run
        if not last_run_ts or post_ts > last_run_ts.astimezone(timezone.utc):
            new_root_posts.append(item)

if not new_root_posts:
    print("No new posts to sync. Exiting.")
    exit()

print(f"Found {len(new_root_posts)} new posts to sync.")

# Sort posts by time ascending to process them in order
new_root_posts.sort(
    key=lambda x: datetime.fromisoformat(
        x.post.record.created_at.replace("Z", "+00:00")
    )
)

for item in new_root_posts:
    post_record = item.post.record
    post_ts = datetime.fromisoformat(post_record.created_at.replace("Z", "+00:00"))

    # Use the first line of text for the slug, or "untitled"
    first_line = post_record.text.split("\n")[0] if post_record.text.strip() else ""
    slug = slugify(first_line)
    filename = f"{post_ts.strftime('%Y-%m-%d')}-{slug}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    print(f"Processing post: {filename}")

    # --- Image Handling Logic ---
    front_matter_images = ""
    post_content_images = ""
    local_image_paths = []

    images = item.post.embed.images if hasattr(item.post.embed, "images") else []

    # Download all images first
    if images:
        for i, img in enumerate(images):
            img_url = img.fullsize
            local_path = download_image(img_url, slug, i)
            if local_path:
                local_image_paths.append(local_path)

    # Conditional logic based on the number of images
    if len(local_image_paths) > 1:
        # More than one image: add to frontmatter
        image_list_yaml = "\n".join([f"  - {p}" for p in local_image_paths])
        front_matter_images = f"images:\n{image_list_yaml}"
    elif len(local_image_paths) == 1:
        # Exactly one image: embed in the post body
        alt_text = first_line or "Blog post image"
        post_content_images = (
            f"![{alt_text}]({local_image_paths[0]}){{: .blog-image .med}}\n"
        )

    # --- File Generation ---
    # Use a generic title, as the content is the main focus
    title = f"Post from {post_ts.strftime('%B %d, %Y')}"

    # Prepare post content
    post_text = post_record.text.strip()
    full_content = f"{post_content_images}{post_text}"

    # Create the file with the appropriate frontmatter and content
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write("layout: microblog_post\n")
        f.write(f'title: "{title}"\n')
        f.write(f"date: {post_ts.strftime('%Y-%m-%d %H:%M:%S %z')}\n")
        if front_matter_images:
            f.write(f"{front_matter_images}\n")
        f.write("---\n\n")
        f.write(full_content)

# After successfully processing all new posts, update the timestamp
# Use the timestamp of the most recent post from this run
if new_root_posts:
    latest_post_ts = datetime.fromisoformat(
        new_root_posts[-1].post.record.created_at.replace("Z", "+00:00")
    )
    save_last_run_timestamp(latest_post_ts)
    print(f"Sync complete. Last run timestamp updated to: {latest_post_ts.isoformat()}")
