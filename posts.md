---
layout: default
title: Posts
display_footer: True
---

<h1>Recent Posts</h1>

<div class="microblog-feed">
  {% for post in site.posts %}
    <article class="microblog-post-preview">
      <header>
        <h2><a href="{{ post.url | relative_url }}" class="microblog-linkout">{{ post.title }}</a></h2>
        <time datetime="{{ post.date | date_to_xmlschema }}">
          {{ post.date | date: "%B %d, %Y at %I:%M %p" }}
        </time>
      </header>

      {%- comment -%} This gallery preview uses the front matter and remains unchanged. {%- endcomment -%}
      {% if post.images %}
        {% include gallery_preview.html images=post.images %}
      {% endif %}

      <div class="microblog-content">
        {%- comment -%} This is the crucial change. It now shows only the content before the "<!--more-->" tag. {%- endcomment -%}
        {{ post.excerpt }}
      </div>
    </article>
  {% endfor %}
</div>