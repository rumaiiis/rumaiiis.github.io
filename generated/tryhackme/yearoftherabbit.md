---
layout: writeup
title: "/yearoftherabbit"
permalink: "/writeups/tryhackme/yearoftherabbit/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Year of the Rabbit"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect yearoftherabbit</p>
  <h1>Year of the Rabbit</h1>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">2 docx note</span>
    <span class="tag">3 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Attack Path Overview</h2>
  <p>Year of the Rabbit typically blends web enumeration, hidden content discovery, weak credential handling, and Linux post-exploitation. The common flow is to pivot from the application layer to a shell and then enumerate carefully for the final escalation route.</p>
  <div class="tag-list">
    <span class="tag">web enumeration</span>
    <span class="tag">hidden-content discovery</span>
    <span class="tag">credential abuse</span>
    <span class="tag">Linux post-exploitation</span>
  </div>
</section>

## Operator Notes

## Recon

- Initial web enumeration appears ordinary until the static content and media assets are inspected more closely.
- The room deliberately hides the useful path behind redirections, asset references, and content that only becomes obvious after interception and careful review.

## Initial Access

- The intended route is to recover the hidden directory from the web flow, extract the FTP username and password material from the staged artifact, and brute-force or validate FTP access.
- Further artifact analysis on the downloaded file yields the SSH credentials for the next user context.

## Privilege Escalation

- After the SSH foothold, local enumeration and the hidden `s3cr3t` clue expose the path to the next user and finally to root.
- The final escalation hinges on a vulnerable `sudo` path combined with an allowed editor or delegated command.

## Defensive Takeaway

- Static assets, redirects, and media files can leak as much as dynamic endpoints when attackers inspect them properly.
- Obscure encodings and esoteric formats are not protection; they only delay basic analysis.
- Old `sudo` edge cases and delegated editor access remain dangerous escalation primitives.
## Evidence Pack

### gobuster-initial

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.96.124
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/06/28 23:14:16 Starting gobuster in directory enumeration mode
===============================================================

/assets               (Status: 301) [Size: 313] [--> http://10.10.96.124/assets/]

/server-status        (Status: 403) [Size: 277]                                  
===============================================================
2021/06/28 23:56:49 Finished
===============================================================
```

### nmap-full-port

```text
# Nmap 7.91 scan initiated Mon Jun 28 23:16:21 2021 as: nmap -sV -p- -oN nmap-full-port 10.10.96.124
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Mon Jun 28 23:10:04 2021 as: nmap -sV -sC -oN nmap-initial 10.10.96.124
Nmap scan report for 10.10.96.124
Host is up (0.49s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.2
22/tcp open  ssh     OpenSSH 6.7p1 Debian 5 (protocol 2.0)
| ssh-hostkey: 
|   1024 a0:8b:6b:78:09:39:03:32:ea:52:4c:20:3e:82:ad:60 (DSA)
|   2048 df:25:d0:47:1f:37:d9:18:81:87:38:76:30:92:65:1f (RSA)
|   256 be:9f:4f:01:4a:44:c8:ad:f5:03:cb:00:ac:8f:49:44 (ECDSA)
|_  256 db:b1:c1:b9:cd:8c:9d:60:4f:f1:98:e2:99:fe:08:03 (ED25519)
80/tcp open  http    Apache httpd 2.4.10 ((Debian))
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: Apache2 Debian Default Page: It works
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jun 28 23:10:41 2021 -- 1 IP address (1 host up) scanned in 37.09 seconds
```
