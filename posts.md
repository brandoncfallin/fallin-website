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
      <div class="microblog-content">
        {% if post.type == "longform" %}
          {% if post.excerpt %}
            {{ post.excerpt }}
            <p><a href="{{ post.url | relative_url }}">Continue reading...</a></p>
          {% else %}
            {{ post.content }} {# Fallback for longform posts without an explicit excerpt marker #}
          {% endif %}
        {% else %}
          {{ post.content }} 
        {% endif %}
      </div>
    </article>
  {% endfor %}
</div>