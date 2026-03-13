---
layout: page
title: "/colddbox-easy"
permalink: "/writeups/tryhackme/colddbox-easy/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "ColddBox Easy"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect colddbox-easy</p>
  <h1>ColddBox Easy</h1>
  <p>Linux room covering service enumeration, initial access, and privilege escalation. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">3 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>ColddBox Easy is generally approached by enumerating WordPress, finding weak or reused credentials, leveraging the application for initial access, and then escalating locally through misconfiguration or exposed credential material on the box.</p>
  <div class="tag-list">
    <span class="tag">WordPress enumeration</span>
    <span class="tag">credential abuse</span>
    <span class="tag">web-to-shell workflow</span>
    <span class="tag">local privilege escalation</span>
  </div>
</section>

## Notes

## Recon

- ColddBox Easy is best approached through structured enumeration rather than noisy exploitation.
- The early workflow usually centers on WordPress enumeration, credential abuse, which exposes the route into the room.

## Initial Access

- The intended foothold comes from following the attack path described in the room flow and validating the exposed service behavior.
- In practice, this means converting the discovered clues into working access through WordPress enumeration and adjacent enumeration findings.

## Privilege Escalation

- After the first foothold, the room shifts into post-exploitation and local review.
- The key escalation themes are web-to-shell workflow, local privilege escalation, which complete the move to the final proof material.

## Security Notes

- ColddBox Easy reinforces how small exposure points compound when enumeration is disciplined and service relationships are understood.
- The defensive lesson is to reduce credential reuse, remove unnecessary trust paths, and harden secondary services before they become the pivot.
## Collected Output

### gobuster-initial

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.224.114
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/07/08 16:48:06 Starting gobuster in directory enumeration mode
===============================================================

/.hta                 (Status: 403) [Size: 278]

/.htaccess            (Status: 403) [Size: 278]

/.htpasswd            (Status: 403) [Size: 278]

/hidden               (Status: 301) [Size: 315] [--> http://10.10.224.114/hidden/]

/server-status        (Status: 403) [Size: 278]                                   

/wp-admin             (Status: 301) [Size: 317] [--> http://10.10.224.114/wp-admin/]

/wp-content           (Status: 301) [Size: 319] [--> http://10.10.224.114/wp-content/]

/wp-includes          (Status: 301) [Size: 320] [--> http://10.10.224.114/wp-includes/]

/xmlrpc.php           (Status: 200) [Size: 42]                                         
===============================================================
2021/07/08 16:49:01 Finished
===============================================================
```

### nmap-full_port

```text
# Nmap 7.91 scan initiated Thu Jul  8 17:03:24 2021 as: nmap -p- -oN nmap-full_port -vv 10.10.224.114
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Thu Jul  8 16:47:02 2021 as: nmap -sV -sC -oN nmap-initial 10.10.224.114
Nmap scan report for 10.10.224.114
Host is up (0.58s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-generator: WordPress 4.1.31
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: ColddBox | One more machine

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jul  8 16:47:42 2021 -- 1 IP address (1 host up) scanned in 40.41 seconds
```
