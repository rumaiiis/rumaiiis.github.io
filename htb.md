---
layout: page
title: /htb
permalink: /writeups/htb/
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# open archive://hackthebox</p>
  <h1>Hack The Box</h1>
  <p>Selected HTB notes rewritten into cleaner operator-focused writeups. The goal is to show methodology, not raw challenge answers.</p>
</section>

<section class="panel">
  <h2>Oopsie</h2>
  <p class="writeup-meta">Web exploitation | session abuse | lateral privilege use</p>
  <p><strong>Room Profile:</strong> Compact web box that rewards methodical endpoint discovery, session manipulation, and practical post-auth abuse instead of noisy exploitation.</p>
  <p><strong>Recon:</strong> Initial enumeration identified a public web application with functionality split across standard and hidden routes. The useful path came from checking exposed functionality, response behavior, and access control assumptions rather than from brute forcing blindly.</p>
  <p><strong>Initial Access:</strong> The main foothold came from abusing weak authorization logic. By understanding how the application handled identity and role context, it was possible to pivot from a lower-privileged user workflow into an administrative path.</p>
  <p><strong>Privilege Escalation:</strong> Once authenticated access was obtained, the path centered on finding upload or execution opportunities that could be converted into code execution and then escalating through local weaknesses.</p>
  <p><strong>Defensive Takeaway:</strong> Oopsie is a good reminder that broken access control is often more damaging than a single vulnerable endpoint. Session trust, role validation, and server-side authorization need explicit enforcement.</p>
  <div class="access-links">
    <a href="/writeups/">back to writeups</a>
  </div>
</section>
