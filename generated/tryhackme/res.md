---
layout: writeup
title: "/res"
permalink: "/writeups/tryhackme/res/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Res"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect res</p>
  <h1>Res</h1>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">2 docx note</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Workflow Focus</h2>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Operator Notes

## Recon

- This room follows the usual Linux boot-to-root pattern where service enumeration and artifact review reveal the access path.
- Res rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The initial foothold comes from exposed services, leaked files, or weak credentials rather than blind exploitation.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- Privilege escalation depends on local enumeration, trust abuse, writable automation, or delegated execution paths on the host.
- After the foothold, local context matters more than noisy exploitation.

## Defensive Takeaway

- The defensive lesson is that Linux post-exploitation paths are usually avoidable with better secret handling and tighter local permissions.
## Evidence Pack

### nmap-initial

```text
# Nmap 7.91 scan initiated Sun Jun 20 22:16:05 2021 as: nmap -sS -sV -sC -vv -oN ./nmap-initial 10.10.156.36
Nmap scan report for 10.10.156.36
Host is up, received timestamp-reply ttl 61 (0.61s latency).
Scanned at 2021-06-20 22:16:07 IST for 110s
Not shown: 999 closed ports
Reason: 999 resets
PORT   STATE SERVICE REASON         VERSION
80/tcp open  http    syn-ack ttl 61 Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jun 20 22:17:58 2021 -- 1 IP address (1 host up) scanned in 112.99 seconds
```
