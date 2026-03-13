---
layout: page
title: "/source"
permalink: "/writeups/tryhackme/source/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Source"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect source</p>
  <h1>Source</h1>
  <p>Web-focused room covering application testing, content discovery, and common attack paths. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Web and App Security</strong>.</p>
  <div class="tag-list">
    <span class="tag">Web and App Security</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">2 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Web-focused room covering application testing, content discovery, and common attack paths. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Notes

## Recon

- The web application is the main attack surface, so content discovery, login behavior, and hidden paths matter immediately.
- Source rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The intended foothold comes from chaining application flaws, exposed content, or weak credentials into code execution or authenticated access.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- Once the app is compromised, the next step is to stabilize host access and enumerate for the final path to proof material.
- After the foothold, local context matters more than noisy exploitation.

## Security Notes

- The defensive lesson is that web compromise rarely stays in the web tier when secrets, upload paths, or admin functions are exposed.
## Collected Output

### nmap-full-port

```text
# Nmap 7.91 scan initiated Tue Jul  6 21:36:13 2021 as: nmap -sV -p- -vv -oN nmap-full-port 10.10.227.239
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Tue Jul  6 21:34:34 2021 as: nmap -sV -sC -oN nmap-initial 10.10.227.239
Nmap scan report for 10.10.227.239
Host is up (0.47s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b7:4c:d0:bd:e2:7b:1b:15:72:27:64:56:29:15:ea:23 (RSA)
|   256 b7:85:23:11:4f:44:fa:22:00:8e:40:77:5e:cf:28:7c (ECDSA)
|_  256 a9:fe:4b:82:bf:89:34:59:36:5b:ec:da:c2:d3:95:ce (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jul  6 21:35:04 2021 -- 1 IP address (1 host up) scanned in 30.95 seconds
```
