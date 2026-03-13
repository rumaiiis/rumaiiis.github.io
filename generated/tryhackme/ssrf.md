---
layout: writeup
title: "/ssrf"
permalink: "/writeups/tryhackme/ssrf/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "SSRF"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect ssrf</p>
  <h1>SSRF</h1>
  <p>Web-facing lab centered on application testing, content discovery, misconfiguration abuse, and foothold development. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Web and App Security</strong>.</p>
  <div class="tag-list">
    <span class="tag">Web and App Security</span>
    <span class="tag">1 docx note</span>
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
- SSRF rewards careful note-taking and stepwise validation rather than trial-and-error execution.

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
# Nmap 7.91 scan initiated Sun Jun 20 11:24:04 2021 as: nmap -sS -sV -sC -vv -oN ./nmap-initial 10.10.159.15
Nmap scan report for 10.10.159.15
Host is up, received echo-reply ttl 61 (0.53s latency).
Scanned at 2021-06-20 11:24:07 IST for 33s
Not shown: 997 closed ports
Reason: 997 resets
PORT     STATE SERVICE REASON         VERSION
22/tcp   open  ssh     syn-ack ttl 61 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 68:72:c3:c0:53:b8:31:77:d7:d0:ad:dc:be:7d:cc:d2 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCe3FuzlF3QOb2x2QFTXYf15QcO8JGJJAJnvv3OMDV7+lAuJh1tQXAuqyEG4UXMuRqyHeQQjYXcXNlGPKDKMV0WTN8GWv9R3dyg3FYsqIQyz/q6NAeGIlb2oUK6mpDj1oOQlMtl9/ORMP+Rx9yc7FKNDxIwwgNqKeCowk4X3Hgj5QvSFBinlHvzZW5LLneZSSngx7O+x1OAJlBDf9qSls6cW0qtpvJ9YsO5hKPLBOkR2BFRCDeLl3rTHgAH3ZhZa5l9dHRkEPh1POZKX6fo0L1QwF0eUcJBOm6bpjZLK0S109FmlAjWgx+T1JYRihRsOmZUWZEvHhKegK+d/1rRd7z7
|   256 7d:5b:c3:14:c7:86:df:90:f7:31:43:f8:b9:09:04:e4 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBG16kzU7fGAINJ0ZpRCFdOgoOxmkh3WiYb2OXcJChcZNyNNFe1PbkbebGlkag0EHn2WydcjCdXKyLaXDtFHcFt4=
|   256 40:d6:4a:57:98:40:5b:84:d8:06:8f:7d:49:fe:e7:3b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDc22nrpKcLefmD318ZTPAg0FZoRNbxM5zfeSiVFcgKq
5000/tcp open  http    syn-ack ttl 61 Werkzeug httpd 0.14.1 (Python 3.6.9)
| http-methods: 
|_  Supported Methods: HEAD GET OPTIONS
|_http-title: Live demonstrations
8000/tcp open  http    syn-ack ttl 61 Werkzeug httpd 0.14.1 (Python 3.6.9)
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET
|_http-title: Live demonstrations
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jun 20 11:24:40 2021 -- 1 IP address (1 host up) scanned in 36.64 seconds
```
