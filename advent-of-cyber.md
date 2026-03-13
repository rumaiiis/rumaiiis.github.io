---
layout: page
title: /advent
permalink: /writeups/advent-of-cyber/
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# query writeups --series seasonal</p>
  <h1>Advent and Seasonal Challenges</h1>
  <p>TryHackMe seasonal challenge archives including Advent of Cyber and similar event-based learning tracks.</p>
</section>

{% assign seasonal_posts = site.posts | where_exp: "post", "post.writeup_type == 'seasonal'" %}
{% assign grouped_series = seasonal_posts | group_by: "series" %}

{% for group in grouped_series %}
<section class="panel">
  <h2>{{ group.name }}</h2>
  <div class="writeup-list">
    {% for post in group.items %}
      <article class="writeup-card">
        <span class="writeup-label">Seasonal</span>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p class="writeup-meta">{{ post.event_day }}</p>
        <p>{{ post.excerpt | strip_html | truncate: 180 }}</p>
      </article>
    {% endfor %}
  </div>
</section>
{% endfor %}
