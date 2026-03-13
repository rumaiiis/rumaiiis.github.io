---
layout: writeup
title: "/team"
permalink: "/writeups/tryhackme/team/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Team"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect team</p>
  <h1>Team</h1>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">4 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Attack Path Overview</h2>
  <p>Team generally follows a web-to-SSH Linux path: use web enumeration to recover hints or local file access, obtain credentials or a user foothold, transition into SSH, and escalate via writable scripts or trusted execution paths.</p>
  <div class="tag-list">
    <span class="tag">web enumeration</span>
    <span class="tag">file access abuse</span>
    <span class="tag">credential recovery</span>
    <span class="tag">SSH foothold</span>
    <span class="tag">Linux privesc</span>
  </div>
</section>

## Operator Notes

## Recon

- The visible site looks almost like a default Apache page, but the hostname clue in the title is the first real step in the room.
- Once the host entry is added, directory and virtual-host enumeration expose the useful application content and user context.

## Initial Access

- The room is solved by combining web clues, local-file-read behavior, and credential recovery rather than brute force alone.
- After the right user context is recovered, the path transitions into SSH for a stable Linux foothold.

## Privilege Escalation

- Post-exploitation focuses on writable scripts or trusted execution paths that run under a higher-privilege user.
- The box rewards careful inspection of local automation and delegated execution rather than noisy exploitation.

## Defensive Takeaway

- Small hostname clues can hide the real attack surface from casual testing, but not from structured enumeration.
- File-read issues frequently become credential compromise once application data and local scripts are exposed.
- Trusted scripts and scheduled execution paths need the same hardening attention as public-facing services.
## Evidence Pack

### gobuster-host

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://team.thm
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/07/22 00:53:44 Starting gobuster in directory enumeration mode
===============================================================

/.hta                 (Status: 403) [Size: 273]

/.htpasswd            (Status: 403) [Size: 273]

/.htaccess            (Status: 403) [Size: 273]

/assets               (Status: 301) [Size: 305] [--> http://team.thm/assets/]

/images               (Status: 301) [Size: 305] [--> http://team.thm/images/]

/index.html           (Status: 200) [Size: 2966]                             

/robots.txt           (Status: 200) [Size: 5]                                

/scripts              (Status: 301) [Size: 306] [--> http://team.thm/scripts/]

/server-status        (Status: 403) [Size: 273]                               
===============================================================
2021/07/22 00:54:34 Finished
===============================================================
```

### gobuster-host-2

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://team.thm/scripts/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/07/22 01:08:35 Starting gobuster in directory enumeration mode
===============================================================

/.htpasswd            (Status: 403) [Size: 273]

/.hta                 (Status: 403) [Size: 273]

/.htaccess            (Status: 403) [Size: 273]
===============================================================
2021/07/22 01:09:31 Finished
===============================================================
```

### gobuster-initial

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.29.93
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/07/22 00:49:05 Starting gobuster in directory enumeration mode
===============================================================

/.htaccess            (Status: 403) [Size: 276]

/.htpasswd            (Status: 403) [Size: 276]

/.hta                 (Status: 403) [Size: 276]

/index.html           (Status: 200) [Size: 11366]

/server-status        (Status: 403) [Size: 276]  
===============================================================
2021/07/22 00:49:45 Finished
===============================================================
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Thu Jul 22 00:48:38 2021 as: nmap -sV -sC -oN nmap-initial 10.10.29.93
Nmap scan report for 10.10.29.93
Host is up (0.46s latency).
Not shown: 997 filtered ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 79:5f:11:6a:85:c2:08:24:30:6c:d4:88:74:1b:79:4d (RSA)
|   256 af:7e:3f:7e:b4:86:58:83:f1:f6:a2:54:a6:9b:ba:ad (ECDSA)
|_  256 26:25:b0:7b:dc:3f:b2:94:37:12:5d:cd:06:98:c7:9f (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works! If you see this add 'te...
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jul 22 00:50:12 2021 -- 1 IP address (1 host up) scanned in 94.56 seconds
```
