---
layout: page
title: "/adventofcyber-2019"
permalink: "/writeups/tryhackme/adventofcyber-2019/"
platform: "TryHackMe"
writeup_type: "series"
series_name: "Advent of Cyber 2019"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect adventofcyber-2019</p>
  <h1>Advent of Cyber 2019</h1>
  <p>Collection page for Advent of Cyber 2019 with links to the available day-by-day notes.</p>
</section>

{% assign series_posts = site.posts | where: "series", page.series_name %}
<section class="panel">
  <h2>Day Index</h2>
  <div class="writeup-list">
  {% for post in series_posts %}
    <article class="writeup-card">
      <span class="writeup-label">Seasonal</span>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p class="writeup-meta">{{ post.event_day }}</p>
      <p>{{ post.excerpt | strip_html | truncate: 160 }}</p>
    </article>
  {% endfor %}
  </div>
</section>
