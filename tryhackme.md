---
layout: page
title: /tryhackme
permalink: /writeups/tryhackme/
---

{% assign series = site.data.tryhackme_rooms | where: "kind", "series" %}
{% assign windows_ad = site.data.tryhackme_rooms | where: "category", "windows-ad" %}
{% assign web_apps = site.data.tryhackme_rooms | where: "category", "web-apps" %}
{% assign linux_privesc = site.data.tryhackme_rooms | where: "category", "linux-privesc" %}
{% assign recon_fundamentals = site.data.tryhackme_rooms | where: "category", "recon-fundamentals" %}
{% assign challenge_labs = site.data.tryhackme_rooms | where: "category", "challenge-labs" %}
{% assign rooms = site.data.tryhackme_rooms | where: "kind", "room" %}

<section class="page-hero panel" id="top">
  <p class="eyebrow">root@rumais:~# open archive://tryhackme-map</p>
  <h1>TryHackMe Map</h1>
  <p>Visual knowledge map for the complete TryHackMe archive. Rooms are grouped by learning track so visitors can move through Windows, web, Linux, recon, and challenge labs without scanning one long page.</p>
</section>

<section class="archive-shell">
<article class="panel explorer-shell">
  <div class="explorer-toolbar">
    <input id="thm-search" class="archive-search" type="text" placeholder="search room, category, or keyword">
    <div class="archive-switches">
      <button class="archive-filter is-active" type="button" data-filter="all">all</button>
      <button class="archive-filter" type="button" data-filter="seasonal-events">seasonal</button>
      <button class="archive-filter" type="button" data-filter="windows-ad">windows + ad</button>
      <button class="archive-filter" type="button" data-filter="web-apps">web apps</button>
      <button class="archive-filter" type="button" data-filter="linux-privesc">linux + privesc</button>
      <button class="archive-filter" type="button" data-filter="recon-fundamentals">recon</button>
      <button class="archive-filter" type="button" data-filter="challenge-labs">challenge labs</button>
    </div>
  </div>

  <div class="tree-nav compact-tree">
    <div class="tree-node">
      <span class="tree-root">/writeups/tryhackme</span>
    </div>
    <div class="tree-branch">
      <a class="tree-link" href="#seasonal-events">
        <strong>Seasonal Events</strong>
        <span>{{ series | size }} series</span>
      </a>
    </div>
    <div class="tree-branch">
      <a class="tree-link" href="#windows-ad">
        <strong>Windows and AD</strong>
        <span>{{ windows_ad | size }} rooms</span>
      </a>
    </div>
    <div class="tree-branch">
      <a class="tree-link" href="#web-apps">
        <strong>Web and App Security</strong>
        <span>{{ web_apps | size }} rooms</span>
      </a>
    </div>
    <div class="tree-branch">
      <a class="tree-link" href="#linux-privesc">
        <strong>Linux and PrivEsc</strong>
        <span>{{ linux_privesc | size }} rooms</span>
      </a>
    </div>
    <div class="tree-branch">
      <a class="tree-link" href="#recon-fundamentals">
        <strong>Recon and Fundamentals</strong>
        <span>{{ recon_fundamentals | size }} rooms</span>
      </a>
    </div>
    <div class="tree-branch">
      <a class="tree-link" href="#challenge-labs">
        <strong>Challenge Labs</strong>
        <span>{{ challenge_labs | size }} rooms</span>
      </a>
    </div>
  </div>
</article>

<article class="panel">
  <div class="map-grid map-grid-tight">
    <a class="map-card" href="#seasonal-events">
      <span class="writeup-label">Series</span>
      <strong>{{ series | size }}</strong>
      <h2>Seasonal Events</h2>
      <p>Advent of Cyber collections and day tracks.</p>
    </a>
    <a class="map-card" href="#windows-ad">
      <span class="writeup-label">Track</span>
      <strong>{{ windows_ad | size }}</strong>
      <h2>Windows and AD</h2>
      <p>SMB, Windows exploitation, and directory services.</p>
    </a>
    <a class="map-card" href="#web-apps">
      <span class="writeup-label">Track</span>
      <strong>{{ web_apps | size }}</strong>
      <h2>Web and App Security</h2>
      <p>Browser-facing attack paths and app flaws.</p>
    </a>
    <a class="map-card" href="#linux-privesc">
      <span class="writeup-label">Track</span>
      <strong>{{ linux_privesc | size }}</strong>
      <h2>Linux and PrivEsc</h2>
      <p>Footholds, enumeration, and shell-to-root paths.</p>
    </a>
    <a class="map-card" href="#recon-fundamentals">
      <span class="writeup-label">Track</span>
      <strong>{{ recon_fundamentals | size }}</strong>
      <h2>Recon and Fundamentals</h2>
      <p>Network basics, cracking, tooling, and recon labs.</p>
    </a>
    <a class="map-card" href="#challenge-labs">
      <span class="writeup-label">Track</span>
      <strong>{{ challenge_labs | size }}</strong>
      <h2>Challenge Labs</h2>
      <p>Mixed boxes and wider CTF-style exercises.</p>
    </a>
  </div>
</article>
</section>

<details class="panel tree-section thm-entry-group" id="seasonal-events" open>
  <summary class="tree-summary">
    <div>
      <p class="eyebrow">Series</p>
      <h2>Seasonal Events</h2>
      <p>Event-based collections with daily challenge flow and a guided archive feel.</p>
    </div>
    <span class="section-jump">{{ series | size }} entries</span>
  </summary>
  <div class="track-grid tree-leaf-grid">
    {% for item in series %}
      <article class="track-tile thm-entry" data-name="{{ item.display_name | downcase }}" data-kind="{{ item.kind }}" data-coverage="{{ item.coverage }}" data-group="{{ item.category }}">
        <a href="{{ item.url | relative_url }}" class="room-link">
          <span class="room-state">{{ item.kind }}</span>
          <h3>{{ item.display_name }}</h3>
          <p class="writeup-meta">{{ item.markdown_count }} markdown | {{ item.note_count }} note files</p>
        </a>
      </article>
    {% endfor %}
  </div>
  <div class="access-links compact-links">
    <a href="#top">back to top</a>
  </div>
</details>

<details class="panel tree-section thm-entry-group" id="windows-ad" open>
  <summary class="tree-summary">
    <div>
      <p class="eyebrow">Track</p>
      <h2>Windows and AD</h2>
      <p>Windows attack surface, SMB workflow, service abuse, and Active Directory practice.</p>
    </div>
    <span class="section-jump">{{ windows_ad | size }} entries</span>
  </summary>
  <div class="track-grid tree-leaf-grid">
    {% for item in windows_ad %}
      <article class="track-tile thm-entry" data-name="{{ item.display_name | downcase }}" data-kind="{{ item.kind }}" data-coverage="{{ item.coverage }}" data-group="{{ item.category }}">
        <a href="{{ item.url | relative_url }}" class="room-link">
          <span class="room-state">{{ item.category_title }}</span>
          <h3>{{ item.display_name }}</h3>
          <p class="writeup-meta">md {{ item.markdown_count }} | docx {{ item.docx_count }} | notes {{ item.note_count }}</p>
        </a>
      </article>
    {% endfor %}
  </div>
  <div class="access-links compact-links">
    <a href="#top">back to top</a>
  </div>
</details>

<details class="panel tree-section thm-entry-group" id="web-apps" open>
  <summary class="tree-summary">
    <div>
      <p class="eyebrow">Track</p>
      <h2>Web and App Security</h2>
      <p>Application testing workflow, browser attack paths, web enumeration, and exploitation practice.</p>
    </div>
    <span class="section-jump">{{ web_apps | size }} entries</span>
  </summary>
  <div class="track-grid tree-leaf-grid">
    {% for item in web_apps %}
      <article class="track-tile thm-entry" data-name="{{ item.display_name | downcase }}" data-kind="{{ item.kind }}" data-coverage="{{ item.coverage }}" data-group="{{ item.category }}">
        <a href="{{ item.url | relative_url }}" class="room-link">
          <span class="room-state">{{ item.category_title }}</span>
          <h3>{{ item.display_name }}</h3>
          <p class="writeup-meta">md {{ item.markdown_count }} | docx {{ item.docx_count }} | notes {{ item.note_count }}</p>
        </a>
      </article>
    {% endfor %}
  </div>
  <div class="access-links compact-links">
    <a href="#top">back to top</a>
  </div>
</details>

<details class="panel tree-section thm-entry-group" id="linux-privesc" open>
  <summary class="tree-summary">
    <div>
      <p class="eyebrow">Track</p>
      <h2>Linux and PrivEsc</h2>
      <p>Linux service enumeration, initial footholds, and common shell-to-root escalation paths.</p>
    </div>
    <span class="section-jump">{{ linux_privesc | size }} entries</span>
  </summary>
  <div class="track-grid tree-leaf-grid">
    {% for item in linux_privesc %}
      <article class="track-tile thm-entry" data-name="{{ item.display_name | downcase }}" data-kind="{{ item.kind }}" data-coverage="{{ item.coverage }}" data-group="{{ item.category }}">
        <a href="{{ item.url | relative_url }}" class="room-link">
          <span class="room-state">{{ item.category_title }}</span>
          <h3>{{ item.display_name }}</h3>
          <p class="writeup-meta">md {{ item.markdown_count }} | docx {{ item.docx_count }} | notes {{ item.note_count }}</p>
        </a>
      </article>
    {% endfor %}
  </div>
  <div class="access-links compact-links">
    <a href="#top">back to top</a>
  </div>
</details>

<details class="panel tree-section thm-entry-group" id="recon-fundamentals" open>
  <summary class="tree-summary">
    <div>
      <p class="eyebrow">Track</p>
      <h2>Recon and Fundamentals</h2>
      <p>Network foundations, recon workflow, cracking exercises, and security tooling labs.</p>
    </div>
    <span class="section-jump">{{ recon_fundamentals | size }} entries</span>
  </summary>
  <div class="track-grid tree-leaf-grid">
    {% for item in recon_fundamentals %}
      <article class="track-tile thm-entry" data-name="{{ item.display_name | downcase }}" data-kind="{{ item.kind }}" data-coverage="{{ item.coverage }}" data-group="{{ item.category }}">
        <a href="{{ item.url | relative_url }}" class="room-link">
          <span class="room-state">{{ item.category_title }}</span>
          <h3>{{ item.display_name }}</h3>
          <p class="writeup-meta">md {{ item.markdown_count }} | docx {{ item.docx_count }} | notes {{ item.note_count }}</p>
        </a>
      </article>
    {% endfor %}
  </div>
  <div class="access-links compact-links">
    <a href="#top">back to top</a>
  </div>
</details>

<details class="panel tree-section thm-entry-group" id="challenge-labs" open>
  <summary class="tree-summary">
    <div>
      <p class="eyebrow">Track</p>
      <h2>Challenge Labs</h2>
      <p>Mixed challenge boxes, compact CTF labs, and broader practice sets that cut across topics.</p>
    </div>
    <span class="section-jump">{{ challenge_labs | size }} entries</span>
  </summary>
  <div class="track-grid tree-leaf-grid">
    {% for item in challenge_labs %}
      <article class="track-tile thm-entry" data-name="{{ item.display_name | downcase }}" data-kind="{{ item.kind }}" data-coverage="{{ item.coverage }}" data-group="{{ item.category }}">
        <a href="{{ item.url | relative_url }}" class="room-link">
          <span class="room-state">{{ item.category_title }}</span>
          <h3>{{ item.display_name }}</h3>
          <p class="writeup-meta">md {{ item.markdown_count }} | docx {{ item.docx_count }} | notes {{ item.note_count }}</p>
        </a>
      </article>
    {% endfor %}
  </div>
  <div class="access-links compact-links">
    <a href="#top">back to top</a>
  </div>
</details>

<section class="panel archive-empty" id="thm-empty-state" hidden>
  <h2>No Matches</h2>
  <p>No room or series matched the current search term.</p>
</section>

<script src="{{ '/assets/tryhackme-archive.js' | relative_url }}"></script>
