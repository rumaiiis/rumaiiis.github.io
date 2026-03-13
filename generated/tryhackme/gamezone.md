---
layout: page
title: "/gamezone"
permalink: "/writeups/tryhackme/gamezone/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Game Zone"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect gamezone</p>
  <h1>Game Zone</h1>
  <p>Web-focused room covering application testing, content discovery, and common attack paths. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Web and App Security</strong>.</p>
  <div class="tag-list">
    <span class="tag">Web and App Security</span>
    <span class="tag">3 docx note</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>GameZone is usually solved by enumerating the login workflow, exploiting injection or weak validation in the web layer, recovering database-backed information, and using that access to transition into host-level compromise.</p>
  <div class="tag-list">
    <span class="tag">web login analysis</span>
    <span class="tag">injection testing</span>
    <span class="tag">database extraction</span>
    <span class="tag">web-to-host pivot</span>
  </div>
</section>

## Notes

## Recon

- The visible application is the real attack surface, so the first step is to inspect login behavior and input handling rather than hunt for hidden services.
- SQL injection against the login or search workflow is the intended pivot into the backend data.

## Initial Access

- After authentication bypass or injection succeeds, the database content yields the hash and username needed for the next stage.
- Once the recovered secret is cracked, SSH access provides the Linux foothold.

## Privilege Escalation

- Post-login enumeration reveals an internally exposed management interface, typically Webmin, running in a way that can be leveraged locally.
- That local management surface is then used to escalate from user to root.

## Security Notes

- Authentication forms are high-value attack paths because a single injection flaw can hand over both app and host access.
- Database-backed secrets remain highly dangerous when users reuse them for SSH or administration.
- Local-only admin services are still critical exposure if an attacker can land even a basic shell first.

## Supporting Files

### Request

POST /portal.php HTTP/1.1
Host: 10.10.150.4
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 15
Origin: http://10.10.150.4
Connection: close
Referer: http://10.10.150.4/portal.php
Cookie: PHPSESSID=r56osi3hnk89ibtivpj4kadud7
Upgrade-Insecure-Requests: 1
searchitem=test

## Collected Output

### nmap-initial

```text
# Nmap 7.91 scan initiated Sat Jun 26 20:33:50 2021 as: nmap -sC -sV -oN nmap-initial 10.10.150.4
Nmap scan report for 10.10.150.4
Host is up (0.59s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 61:ea:89:f1:d4:a7:dc:a5:50:f7:6d:89:c3:af:0b:03 (RSA)
|   256 b3:7d:72:46:1e:d3:41:b6:6a:91:15:16:c9:4a:a5:fa (ECDSA)
|_  256 53:67:09:dc:ff:fb:3a:3e:fb:fe:cf:d8:6d:41:27:ab (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Game Zone
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jun 26 20:34:32 2021 -- 1 IP address (1 host up) scanned in 42.88 seconds
```
