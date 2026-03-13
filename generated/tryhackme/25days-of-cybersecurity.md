---
layout: writeup
title: "/25days-of-cybersecurity"
permalink: "/writeups/tryhackme/25days-of-cybersecurity/"
platform: "TryHackMe"
writeup_type: "series"
series_name: "Advent of Cyber 2020"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect 25days-of-cybersecurity</p>
  <h1>Advent of Cyber 2020</h1>
  <p>Series archive for Advent of Cyber 2020. Use this as a structured entry point into the seasonal challenge notes and day-wise writeups.</p>
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
