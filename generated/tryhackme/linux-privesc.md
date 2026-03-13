---
layout: writeup
title: "/linux-privesc"
permalink: "/writeups/tryhackme/linux-privesc/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Linux Privesc"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect linux-privesc</p>
  <h1>Linux Privesc</h1>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">3 docx note</span>
  </div>
</section>

<section class="panel">
  <h2>Workflow Focus</h2>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Operator Notes

## Recon

- This room follows the usual Linux boot-to-root pattern where service enumeration and artifact review reveal the access path.
- Linux Privesc rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The initial foothold comes from exposed services, leaked files, or weak credentials rather than blind exploitation.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- Privilege escalation depends on local enumeration, trust abuse, writable automation, or delegated execution paths on the host.
- After the foothold, local context matters more than noisy exploitation.

## Defensive Takeaway

- The defensive lesson is that Linux post-exploitation paths are usually avoidable with better secret handling and tighter local permissions.

## Supporting Notes

### Checklists

Checklists are a good way to make sure you haven't missed anything during your enumeration stage, and also to provide you with a resource to check how to do things if you forget exactly what commands to use
https://github.com/netbiosX/Checklists/blob/master/Linux-Privilege-Escalation.md
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md
https://sushant747.gitbooks.io/total-oscp-guide/privilege_escalation_-_linux.html
https://payatu.com/guide-linux-privilege-escalation
