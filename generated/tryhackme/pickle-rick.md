---
layout: page
title: "/pickle-rick"
permalink: "/writeups/tryhackme/pickle-rick/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Pickle Rick"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect pickle-rick</p>
  <h1>Pickle Rick</h1>
  <p>Linux room covering service enumeration, initial access, and privilege escalation. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">1 docx note</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Linux room covering service enumeration, initial access, and privilege escalation. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Notes

## Recon

- This room follows the usual Linux boot-to-root pattern where service enumeration and artifact review reveal the access path.
- Pickle Rick rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The initial foothold comes from exposed services, leaked files, or weak credentials rather than blind exploitation.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- Privilege escalation depends on local enumeration, trust abuse, writable automation, or delegated execution paths on the host.
- After the foothold, local context matters more than noisy exploitation.

## Security Notes

- The defensive lesson is that Linux post-exploitation paths are usually avoidable with better secret handling and tighter local permissions.
## Collected Output

### nmap-initial

```text
# Nmap 7.91 scan initiated Sat Jun 12 23:06:10 2021 as: nmap -sC -sV -oN ./nmap-initial 10.10.156.83
Nmap scan report for 10.10.156.83
Host is up (0.50s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 ba:06:f4:bc:39:ad:6f:be:e9:08:e0:aa:82:d8:03:68 (RSA)
|   256 6a:ef:d0:62:be:ea:15:f5:72:14:04:3b:83:d7:3d:92 (ECDSA)
|_  256 c6:2a:5e:2d:4b:e0:1b:04:65:51:9e:ef:83:b5:8b:95 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Rick is sup4r cool
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jun 12 23:06:40 2021 -- 1 IP address (1 host up) scanned in 30.09 seconds
```
