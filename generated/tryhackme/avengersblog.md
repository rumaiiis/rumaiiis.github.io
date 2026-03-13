---
layout: writeup
title: "/avengersblog"
permalink: "/writeups/tryhackme/avengersblog/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Avengers Blog"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect avengersblog</p>
  <h1>Avengers Blog</h1>
  <p>Web-facing lab centered on application testing, content discovery, misconfiguration abuse, and foothold development. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Web and App Security</strong>.</p>
  <div class="tag-list">
    <span class="tag">Web and App Security</span>
    <span class="tag">2 docx note</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Workflow Focus</h2>
  <p>Web-facing lab centered on application testing, content discovery, misconfiguration abuse, and foothold development. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Operator Notes

## Recon

- The web application is the main attack surface, so content discovery, login behavior, and hidden paths matter immediately.
- Avengers Blog rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The intended foothold comes from chaining application flaws, exposed content, or weak credentials into code execution or authenticated access.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- Once the app is compromised, the next step is to stabilize host access and enumerate for the final path to proof material.
- After the foothold, local context matters more than noisy exploitation.

## Defensive Takeaway

- The defensive lesson is that web compromise rarely stays in the web tier when secrets, upload paths, or admin functions are exposed.
## Evidence Pack

### nmap-initial

```text
# Nmap 7.91 scan initiated Mon Jun 21 11:02:15 2021 as: nmap -sV -sC -oN ./nmap-initial 10.10.146.7
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
Nmap scan report for 10.10.146.7
Host is up (0.60s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8b:2f:56:dc:82:43:26:20:87:34:e8:af:e9:cc:a2:cf (RSA)
|   256 6b:46:70:9a:ce:de:36:a6:a7:21:a8:ba:fd:01:43:92 (ECDSA)
|_  256 6f:0e:ae:36:09:6a:f0:9b:89:45:58:22:09:f6:59:b0 (ED25519)
80/tcp open  http    Node.js Express framework
|_http-title: Avengers! Assemble!
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jun 21 11:02:57 2021 -- 1 IP address (1 host up) scanned in 41.71 seconds
```
