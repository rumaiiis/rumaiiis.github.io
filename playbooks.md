---
layout: page
title: /playbooks
permalink: /writeups/playbooks/
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# ls /srv/playbooks</p>
  <h1>Playbooks</h1>
  <p>Topic-based notes distilled from INE PTS and PEH lab work. These are structured as reusable workflows rather than challenge-specific answer sheets.</p>
</section>

<section class="writeup-list">
  <article class="panel writeup-card">
    <span class="writeup-label">INE PTS</span>
    <h2>SQL Injection Workflow</h2>
    <p>Start by fingerprinting parameters and request flow, confirm the behavior manually, and only then move into automation. Focus on differentiating reflected input, boolean influence, error-based disclosure, and database-backed behavior before reaching for tooling.</p>
    <p class="writeup-meta">Input validation | manual probing | controlled exploitation</p>
  </article>

  <article class="panel writeup-card">
    <span class="writeup-label">INE PTS</span>
    <h2>Burp Suite Basics</h2>
    <p>Use Burp as a traffic microscope: capture, replay, mutate, and compare. The workflow in the lab centered on hidden routes, debug parameters, and request replay through Proxy, Repeater, and Intruder until sensitive functionality was exposed.</p>
    <p class="writeup-meta">Proxy | Repeater | Intruder | content discovery</p>
  </article>

  <article class="panel writeup-card">
    <span class="writeup-label">INE PTS</span>
    <h2>Scanning and Fingerprinting</h2>
    <p>Move from host discovery into service and OS detection in layers. The key lesson is to correlate ICMP discovery, SYN scan results, service versions, and operating system signals before making assumptions about server and client roles.</p>
    <p class="writeup-meta">fping | nmap -sn | nmap -sS | nmap -sV | nmap -O</p>
  </article>

  <article class="panel writeup-card">
    <span class="writeup-label">INE PTS</span>
    <h2>Nessus Validation Workflow</h2>
    <p>Use discovery to identify the target, profile the exposed services, scope the plugin set to reduce noise, then validate critical findings manually. The value is not the scanner output alone, but the analyst’s ability to verify exploitability and explain risk clearly.</p>
    <p class="writeup-meta">Asset discovery | plugin tuning | validation | reporting</p>
  </article>

  <article class="panel writeup-card">
    <span class="writeup-label">INE PTS</span>
    <h2>Null Session Enumeration</h2>
    <p>Anonymous SMB access can still expose valuable information. The repeatable workflow is: identify SMB services, test null session behavior, enumerate shares and account data, then validate access using smbclient or equivalent tooling.</p>
    <p class="writeup-meta">enum4linux | smbclient | share enumeration</p>
  </article>

  <article class="panel writeup-card">
    <span class="writeup-label">PEH</span>
    <h2>Kioptrix Method Notes</h2>
    <p>This lab is useful for old-school service-driven exploitation. Enumeration linked web disclosure, Samba fingerprinting, and exploit research into a working foothold, with both Metasploit and manual exploitation paths considered.</p>
    <p class="writeup-meta">nikto | samba versioning | exploit validation</p>
  </article>

  <article class="panel writeup-card">
    <span class="writeup-label">PEH</span>
    <h2>Blue Notes</h2>
    <p>Blue remains a good Windows fundamentals lab for learning how service discovery, exploit selection, and post-exploitation fit together in a straightforward workflow.</p>
    <p class="writeup-meta">Windows enumeration | exploit selection | post-exploitation</p>
  </article>

  <article class="panel writeup-card">
    <span class="writeup-label">PEH</span>
    <h2>Juice Shop Workflow</h2>
    <p>Juice Shop is treated here as a controlled target for learning modern web testing habits: map the application, observe client-side behavior, locate hidden features, and tie each bug back to risk rather than just collecting challenge solves.</p>
    <p class="writeup-meta">Web mapping | client-side analysis | OWASP patterns</p>
  </article>
</section>

<section class="panel">
  <h2>Why These Matter</h2>
  <p>These notes sit between offensive training and defensive operations. They show how I document repeatable workflows, reduce noisy experimentation, and convert lab activity into something operationally useful.</p>
</section>
