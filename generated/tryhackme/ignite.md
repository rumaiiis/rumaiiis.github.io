---
layout: writeup
title: "/ignite"
permalink: "/writeups/tryhackme/ignite/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Ignite"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect ignite</p>
  <h1>Ignite</h1>
  <p>Web-facing lab centered on application testing, content discovery, misconfiguration abuse, and foothold development. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Web and App Security</strong>.</p>
  <div class="tag-list">
    <span class="tag">Web and App Security</span>
    <span class="tag">1 docx note</span>
    <span class="tag">2 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Attack Path Overview</h2>
  <p>Ignite is generally a Fuel CMS exploitation room. The normal path is to confirm the vulnerable CMS version, exploit the known RCE issue, establish a shell, harvest local credentials or configuration values, and then escalate on the Linux host.</p>
  <div class="tag-list">
    <span class="tag">Fuel CMS fingerprinting</span>
    <span class="tag">known RCE path</span>
    <span class="tag">shell establishment</span>
    <span class="tag">credential harvesting</span>
    <span class="tag">Linux privesc</span>
  </div>
</section>

## Operator Notes

## Recon

- Ignite is best approached through structured enumeration rather than noisy exploitation.
- The early workflow usually centers on Fuel CMS fingerprinting, known RCE path, which exposes the route into the room.

## Initial Access

- The intended foothold comes from following the attack path described in the room flow and validating the exposed service behavior.
- In practice, this means converting the discovered clues into working access through Fuel CMS fingerprinting and adjacent enumeration findings.

## Privilege Escalation

- After the first foothold, the room shifts into post-exploitation and local review.
- The key escalation themes are shell establishment, credential harvesting, which complete the move to the final proof material.

## Defensive Takeaway

- Ignite reinforces how small exposure points compound when enumeration is disciplined and service relationships are understood.
- The defensive lesson is to reduce credential reuse, remove unnecessary trust paths, and harden secondary services before they become the pivot.
## Evidence Pack

### nmap-full_port

```text
# Nmap 7.91 scan initiated Thu Jun 24 21:47:51 2021 as: nmap -p- -oN nmap-full_port 10.10.57.118
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Thu Jun 24 21:41:14 2021 as: nmap -sC -sV -oN nmap-initial 10.10.57.118
Nmap scan report for 10.10.57.118
Host is up (0.51s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/fuel/
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Welcome to FUEL CMS

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jun 24 21:42:56 2021 -- 1 IP address (1 host up) scanned in 101.70 seconds
```
