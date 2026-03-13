---
layout: writeup
title: "/lazyadmin"
permalink: "/writeups/tryhackme/lazyadmin/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Lazy Admin"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect lazyadmin</p>
  <h1>Lazy Admin</h1>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">1 docx note</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Attack Path Overview</h2>
  <p>Lazy Admin usually starts with CMS enumeration and weak credential handling, then transitions into Linux shell access and a straightforward local privilege-escalation path using exposed scripts, writable files, or sudo misconfiguration.</p>
  <div class="tag-list">
    <span class="tag">CMS enumeration</span>
    <span class="tag">credential recovery</span>
    <span class="tag">Linux foothold</span>
    <span class="tag">local misconfiguration abuse</span>
  </div>
</section>

## Operator Notes

## Recon

- Web enumeration reveals the hidden CMS path quickly, and further content discovery exposes backup and include directories that leak credential material.
- The room rewards directory discovery more than exploit spraying; the data is already present if the paths are found.

## Initial Access

- The exposed backup data yields the administrative credentials for the CMS.
- After logging into the management panel, the intended path is to upload or place a PHP reverse shell and convert application access into a Linux shell.

## Privilege Escalation

- Once on the host, the privilege-escalation route depends on local scripts, weak trust boundaries, or sudo-assisted execution.
- The room is designed to show how quickly a “small” CMS issue becomes full compromise when secrets are exposed.

## Defensive Takeaway

- Backup files inside the web root are effectively credential disclosure.
- CMS admin panels should never have the ability to drop executable content without strict controls.
- Web compromise plus weak local execution rules is enough for total host loss on small Linux deployments.
## Evidence Pack

### nmap-initial

```text
# Nmap 7.91 scan initiated Thu Jun 24 11:13:29 2021 as: nmap -sV -sC -oN nmap-initial 10.10.114.184
Nmap scan report for 10.10.114.184
Host is up (0.47s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 49:7c:f7:41:10:43:73:da:2c:e6:38:95:86:f8:e0:f0 (RSA)
|   256 2f:d7:c4:4c:e8:1b:5a:90:44:df:c0:63:8c:72:ae:55 (ECDSA)
|_  256 61:84:62:27:c6:c3:29:17:dd:27:45:9e:29:cb:90:5e (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jun 24 11:15:27 2021 -- 1 IP address (1 host up) scanned in 118.18 seconds
```
