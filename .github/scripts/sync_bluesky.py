import os
import re
from datetime import datetime

import requests
from atproto import Client

# Configuration
HANDLE = os.getenv("BLUESKY_HANDLE")
APP_PASSWORD = os.getenv("BLUESKY_PASSWORD")
OUTPUT_DIR = "_posts"
IMAGE_DIR = "assets/images/microblog"
SITE_IMAGE_PATH = "/assets/images/microblog"

# Ensure output directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)

# Init client
client = Client()
client.login(HANDLE, APP_PASSWORD)

feed = client.app.bsky.feed.get_author_feed({"actor": HANDLE, "limit": 10})


def slugify(text):
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text[:50] or "untitled"


def download_image(url, slug, index):
    ext = os.path.splitext(url.split("?")[0])[1]
    filename = f"{slug}-{index}{ext}"
    filepath = os.path.join(IMAGE_DIR, filename)
    resp = requests.get(url)
    if resp.ok:
        with open(filepath, "wb") as f:
            f.write(resp.content)
        return f"{SITE_IMAGE_PATH}/{filename}"
    return None


# Count existing Bluesky posts (those with title starting with 'Post #')
post_index = 1
for fname in os.listdir(OUTPUT_DIR):
    if fname.endswith(".md"):
        with open(os.path.join(OUTPUT_DIR, fname)) as f:
            for line in f:
                if line.startswith("title:") and "Post #" in line:
                    post_index += 1
                    break

for item in feed.feed:
    post = item.post.record
    timestamp = datetime.fromisoformat(post.created_at.replace("Z", "+00:00"))
    slug = slugify(post.text.split("\n")[0])
    filename = f"{timestamp.strftime('%Y-%m-%d')}-{slug}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    title_line = f"Post #{post_index:03d}"
    post_index += 1

    content_lines = [post.text.strip()]

    # Handle images
    media = item.post.embed.images if hasattr(item.post.embed, "images") else []
    for i, img in enumerate(media):
        img_url = img.fullsize
        local_path = download_image(img_url, slug, i)
        if local_path:
            content_lines.insert(
                0,
                f"![{slug}]({{ '{{' }} '{local_path}' | relative_url {{ '}}' }}){{: .blog-image .med}}\n",
            )

    with open(filepath, "w") as f:
        f.write(f"""---
layout: microblog_post
title: \"{title_line}\"
date: {timestamp.strftime("%Y-%m-%d %H:%M:%S %z")}
---

{chr(10).join(content_lines)}
""")
