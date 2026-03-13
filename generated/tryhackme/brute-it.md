---
layout: writeup
title: "/brute-it"
permalink: "/writeups/tryhackme/brute-it/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Brute It"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect brute-it</p>
  <h1>Brute It</h1>
  <p>General mixed challenge room blending enumeration, exploitation, and post-exploitation practice. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Challenge Labs</strong>.</p>
  <div class="tag-list">
    <span class="tag">Challenge Labs</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">2 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Attack Path Overview</h2>
  <p>The intended learning path is straightforward web and credential abuse: enumerate services, discover the admin surface, brute-force or recover access, process the RSA material, obtain a user shell, and escalate through the sudo configuration available on the host.</p>
  <div class="tag-list">
    <span class="tag">service enumeration</span>
    <span class="tag">web brute-force</span>
    <span class="tag">RSA key recovery</span>
    <span class="tag">sudo-based privesc</span>
  </div>
</section>

## Operator Notes

## Recon

- Brute It is best approached through structured enumeration rather than noisy exploitation.
- The early workflow usually centers on service enumeration, web brute-force, which exposes the route into the room.

## Initial Access

- The intended foothold comes from following the attack path described in the room flow and validating the exposed service behavior.
- In practice, this means converting the discovered clues into working access through service enumeration and adjacent enumeration findings.

## Privilege Escalation

- After the first foothold, the room shifts into post-exploitation and local review.
- The key escalation themes are RSA key recovery, sudo-based privesc, which complete the move to the final proof material.

## Defensive Takeaway

- Brute It reinforces how small exposure points compound when enumeration is disciplined and service relationships are understood.
- The defensive lesson is to reduce credential reuse, remove unnecessary trust paths, and harden secondary services before they become the pivot.
## Evidence Pack

### gobuster-initial

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.185.219
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/07/08 14:54:52 Starting gobuster in directory enumeration mode
===============================================================

/.hta                 (Status: 403) [Size: 278]

/.htaccess            (Status: 403) [Size: 278]

/.htpasswd            (Status: 403) [Size: 278]

/admin                (Status: 301) [Size: 314] [--> http://10.10.185.219/admin/]

/index.html           (Status: 200) [Size: 10918]                                

/server-status        (Status: 403) [Size: 278]                                  
===============================================================
2021/07/08 14:55:36 Finished
===============================================================
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Thu Jul  8 14:53:54 2021 as: nmap -sV -sC -oN nmap-initial 10.10.185.219
Nmap scan report for 10.10.185.219
Host is up (0.53s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 4b:0e:bf:14:fa:54:b3:5c:44:15:ed:b2:5d:a0:ac:8f (RSA)
|   256 d0:3a:81:55:13:5e:87:0c:e8:52:1e:cf:44:e0:3a:54 (ECDSA)
|_  256 da:ce:79:e0:45:eb:17:25:ef:62:ac:98:f0:cf:bb:04 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jul  8 14:54:31 2021 -- 1 IP address (1 host up) scanned in 36.83 seconds
```
