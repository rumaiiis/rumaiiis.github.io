---
layout: page
title: /writeups
permalink: /writeups/
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# ls /srv/writeups</p>
  <h1>Writeups</h1>
  <p>Curated notes, room writeups, and seasonal challenge archives organized for quick review. The focus is methodology, reasoning, tooling, and lessons learned rather than raw answer dumping.</p>
</section>

{% assign thm_posts = site.posts | where_exp: "post", "post.platform == 'TryHackMe'" %}
{% assign seasonal_posts = site.posts | where_exp: "post", "post.writeup_type == 'seasonal'" %}
{% assign thm_rooms = site.data.tryhackme_rooms | where: "kind", "room" %}
{% assign thm_series = site.data.tryhackme_rooms | where: "kind", "series" %}

<section class="archive-shell">
  <article class="panel">
    <h2>Sections</h2>
    <div class="tree-nav">
      <div class="tree-node">
        <span class="tree-root">/writeups</span>
      </div>
      <div class="tree-branch">
        <a class="tree-link" href="/writeups/tryhackme/">
          <strong>TryHackMe Archive</strong>
          <span>{{ thm_rooms | size }} rooms</span>
        </a>
        <div class="tree-leaf-list">
          <a href="/writeups/advent-of-cyber/">Seasonal Events</a>
          <a href="/writeups/tryhackme/#windows-ad">Windows and AD</a>
          <a href="/writeups/tryhackme/#web-apps">Web and App Security</a>
          <a href="/writeups/tryhackme/#linux-privesc">Linux and PrivEsc</a>
          <a href="/writeups/tryhackme/#recon-fundamentals">Recon and Fundamentals</a>
          <a href="/writeups/tryhackme/#challenge-labs">Challenge Labs</a>
        </div>
      </div>
      <div class="tree-branch">
        <a class="tree-link" href="/writeups/advent-of-cyber/">
          <strong>Seasonal Events</strong>
          <span>{{ thm_series | size }} series | {{ seasonal_posts | size }} posts</span>
        </a>
      </div>
      <div class="tree-branch">
        <a class="tree-link" href="/writeups/htb/">
          <strong>Hack The Box</strong>
          <span>selected writeups</span>
        </a>
      </div>
      <div class="tree-branch">
        <a class="tree-link" href="/writeups/playbooks/">
          <strong>Playbooks</strong>
          <span>reusable notes and workflows</span>
        </a>
      </div>
      <div class="tree-branch">
        <a class="tree-link" href="/writeups/automation/">
          <strong>Automation</strong>
          <span>scripts and helper tools</span>
        </a>
      </div>
      <div class="tree-branch">
        <a class="tree-link" href="/projects/">
          <strong>Projects</strong>
          <span>tool builds and practical utilities</span>
        </a>
      </div>
    </div>
  </article>

  <article class="panel">
    <h2>Collections</h2>
    <div class="collection-grid">
      <a class="collection-card" href="/writeups/tryhackme/">
        <span class="writeup-label">Primary Archive</span>
        <h3>TryHackMe</h3>
        <p>Full room archive grouped by track and searchable from one place.</p>
      </a>
      <a class="collection-card" href="/writeups/advent-of-cyber/">
        <span class="writeup-label">Seasonal</span>
        <h3>Advent of Cyber</h3>
        <p>Event-based day writeups organized as a separate seasonal collection.</p>
      </a>
      <a class="collection-card" href="/writeups/playbooks/">
        <span class="writeup-label">Reusable Notes</span>
        <h3>Playbooks</h3>
        <p>Topic-focused workflows from INE PTS and PEH labs.</p>
      </a>
      <a class="collection-card" href="/writeups/automation/">
        <span class="writeup-label">Tooling</span>
        <h3>Automation</h3>
        <p>Small Bash and Python helpers built around recon and workflow speed.</p>
      </a>
    </div>
  </article>
</section>

<section class="panel">
  <h2>Featured Posts</h2>
  <div class="writeup-list">
    {% for post in thm_posts limit: 8 %}
      <article class="writeup-card">
        <span class="writeup-label">{{ post.platform }}</span>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        {% if post.series %}
          <p class="writeup-meta">{{ post.series }}</p>
        {% endif %}
        <p>{{ post.excerpt | strip_html | truncate: 150 }}</p>
      </article>
    {% endfor %}
  </div>
</section>
