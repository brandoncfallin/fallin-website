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


# Count existing Bluesky posts (those with title starting with 'Post #')
post_index = 1
for fname in os.listdir(OUTPUT_DIR):
    if fname.endswith(".md"):
        with open(os.path.join(OUTPUT_DIR, fname)) as f:
            for line in f:
                if line.startswith("title:") and "Post #" in line:
                    post_index += 1
                    break


def collect_thread_text_and_images(uri, slug):
    thread = client.app.bsky.feed.get_post_thread({"uri": uri})
    segments = []
    image_count = 0

    def walk(node, depth=0):
        nonlocal image_count
        if node.post.author.handle != HANDLE:
            return

        block = []
        content = node.post.record.text.strip()
        block.append(f"> {content}" if depth > 0 else content)

        images = node.post.embed.images if hasattr(node.post.embed, "images") else []
        for i, img in enumerate(images):
            img_url = img.fullsize
            local_path = download_image(img_url, slug, image_count)
            if local_path:
                block.append(f"![{slug}]({local_path}){{: .blog-image .med}}\n")
            image_count += 1

        segments.extend(block)

        for reply in getattr(node, "replies", []) or []:
            walk(reply, depth + 1)

    walk(thread.thread)
    return segments


for item in feed.feed:
    if hasattr(item.post.record, "reply") and item.post.record.reply is not None:
        continue  # Skip replies, only process root posts

    post = item.post.record
    timestamp = datetime.fromisoformat(post.created_at.replace("Z", "+00:00"))
    slug = slugify(post.text.split("\n")[0], limit=30)
    filename = f"{timestamp.strftime('%Y-%m-%d')}-{slug}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    title_line = f"\U0001f535\u2601\ufe0f # {post_index:03d}"
    post_index += 1

    content_lines = collect_thread_text_and_images(item.post.uri, slug)

    with open(filepath, "w") as f:
        f.write(f"""---
layout: microblog_post
title: \"{title_line}\"
date: {timestamp.strftime("%Y-%m-%d %H:%M:%S %z")}
---

{chr(10).join(content_lines)}
""")
