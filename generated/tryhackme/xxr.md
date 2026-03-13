---
layout: page
title: "/xxr"
permalink: "/writeups/tryhackme/xxr/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "XXR"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect xxr</p>
  <h1>XXR</h1>
  <p>Mixed challenge room covering enumeration, exploitation, and post-exploitation practice. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Challenge Labs</strong>.</p>
  <div class="tag-list">
    <span class="tag">Challenge Labs</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Mixed challenge room covering enumeration, exploitation, and post-exploitation practice. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Notes

## Recon

- This room mixes discovery, analysis, and exploitation, so the right path usually appears only after multiple clues are combined.
- XXR rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- Initial access depends on linking those clues together rather than relying on a single obvious vulnerability.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- After the foothold, the room transitions into standard host enumeration and local privilege-escalation review.
- After the foothold, local context matters more than noisy exploitation.

## Security Notes

- The defensive lesson is that seemingly minor leaks across different services often combine into full compromise when an attacker is systematic.
## Collected Output

### nmap-initial

```text
# Nmap 7.91 scan initiated Sun Jun 20 08:45:13 2021 as: nmap -sS -sV -sC -O -oN ./nmap-initial 10.10.174.52
Nmap scan report for 10.10.174.52
Host is up (0.57s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 54:b5:46:93:a1:e6:d6:f5:28:e2:e6:14:af:d0:50:7d (RSA)
|   256 d0:b7:56:c9:11:a6:12:d7:2f:b9:ea:d7:61:23:de:72 (ECDSA)
|_  256 36:55:8b:c6:36:d0:07:18:92:96:b5:4f:a1:9e:d2:f0 (ED25519)
80/tcp open  http    Werkzeug httpd 0.14.1 (Python 3.6.9)
|_http-server-header: Werkzeug/0.14.1 Python/3.6.9
|_http-title: XXE
Aggressive OS guesses: Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Adtran 424RG FTTH gateway (92%), Linux 2.6.32 (92%), Linux 2.6.39 - 3.2 (92%), Linux 3.1 - 3.2 (92%), Linux 3.2 - 4.9 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jun 20 08:46:09 2021 -- 1 IP address (1 host up) scanned in 57.75 seconds
```
