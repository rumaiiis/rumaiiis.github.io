---
layout: page
title: "/rootme"
permalink: "/writeups/tryhackme/rootme/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Root Me"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect rootme</p>
  <h1>Root Me</h1>
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
  <p>Root Me usually follows a file-upload-to-shell path: enumerate the web application, bypass upload filtering, gain a shell on the host, and escalate through SUID or other local privilege-escalation opportunities.</p>
  <div class="tag-list">
    <span class="tag">web enumeration</span>
    <span class="tag">upload bypass</span>
    <span class="tag">web shell execution</span>
    <span class="tag">SUID enumeration</span>
  </div>
</section>

## Notes

## Recon

- Enumeration exposes a straightforward web application and SSH, but the real attack surface is the upload functionality rather than remote login.
- Directory discovery highlights the panel used to submit files and the location where uploaded content becomes accessible.

## Initial Access

- The intended path is to bypass upload restrictions and land a PHP-based reverse shell on the host.
- Once the shell is active, the room shifts into basic Linux enumeration to collect proof artifacts and assess escalation paths.

## Privilege Escalation

- The main privilege-escalation clue is a SUID-enabled binary.
- Abusing the Python SUID path through a GTFOBins technique yields the root shell.

## Security Notes

- Upload validation must include extension handling, execution policy, and storage isolation or it becomes direct code execution.
- Web-to-shell compromise often happens long before defenders notice anything at the SSH layer.
- SUID misconfigurations are high-impact because they turn a basic foothold into full system compromise with minimal noise.
## Collected Output

### nmap-initial

```text
# Nmap 7.91 scan initiated Mon Jun 21 22:04:51 2021 as: nmap -sV -sC -oN ./nmap-initial 10.10.39.34
Nmap scan report for 10.10.39.34
Host is up (0.53s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 4a:b9:16:08:84:c2:54:48:ba:5c:fd:3f:22:5f:22:14 (RSA)
|   256 a9:a6:86:e8:ec:96:c3:f0:03:cd:16:d5:49:73:d0:82 (ECDSA)
|_  256 22:f6:b5:a6:54:d9:78:7c:26:03:5a:95:f3:f9:df:cd (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: HackIT - Home
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jun 21 22:06:25 2021 -- 1 IP address (1 host up) scanned in 94.84 seconds
```
