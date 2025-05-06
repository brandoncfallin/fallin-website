---
layout: default
title: Posts
display_footer: True
---

<h1>Recent Posts</h1>

<div class="microblog-feed">
  {% for post in site.posts reversed %}
    <article class="microblog-post">
      <header>
        <h2>{{ post.subject }}</h2>
        <time datetime="{{ post.date | date_to_xmlschema }}">
          {{ post.date | date: "%B %d, %Y at %I:%M %p" }}
        </time>
      </header>
      <div class="microblog-content">
        {{ post.content }}
      </div>
    </article>
  {% endfor %}
</div>
