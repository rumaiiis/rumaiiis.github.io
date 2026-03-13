---
layout: writeup
title: "/fowsniff-ctf"
permalink: "/writeups/tryhackme/fowsniff-ctf/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Fowsniff CTF"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect fowsniff-ctf</p>
  <h1>Fowsniff CTF</h1>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">2 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Attack Path Overview</h2>
  <p>Fowsniff centers on credential reuse from leaked data. The common path is to gather exposed user information, crack or test recovered passwords, gain shell access through a remote service, and escalate from the low-privilege Linux context.</p>
  <div class="tag-list">
    <span class="tag">OSINT-style data collection</span>
    <span class="tag">password cracking</span>
    <span class="tag">service login</span>
    <span class="tag">Linux privilege escalation</span>
  </div>
</section>

## Operator Notes

## Recon

- The web surface, mail services, and SSH together make this a credential-centric challenge rather than a pure exploit room.
- Public-facing information and leaked employee data are the first practical source of access.

## Initial Access

- The common path is to recover the exposed credential material, crack or test the passwords, access the mailbox, and extract the temporary secret needed for remote login.
- That mailbox-to-SSH pivot is the core transition in the room.

## Privilege Escalation

- Once the low-privilege shell is in place, standard Linux enumeration reveals the privilege-escalation route.
- The challenge is designed around chaining leaked identity data into host compromise, not bypassing patched services.

## Defensive Takeaway

- User-data leaks remain dangerous because they often include just enough material for password recovery and mailbox compromise.
- Email access frequently unlocks the rest of the environment because it becomes the reset and secret-distribution channel.
- Credential hygiene and mailbox protection are part of infrastructure defense, not just user support.
## Evidence Pack

### gobuster-initial

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.107.186
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/07/22 00:21:43 Starting gobuster in directory enumeration mode
===============================================================

/.hta                 (Status: 403) [Size: 292]

/.htaccess            (Status: 403) [Size: 297]

/.htpasswd            (Status: 403) [Size: 297]

/assets               (Status: 301) [Size: 315] [--> http://10.10.107.186/assets/]

/images               (Status: 301) [Size: 315] [--> http://10.10.107.186/images/]

/index.html           (Status: 200) [Size: 2629]                                  

/robots.txt           (Status: 200) [Size: 26]                                    

/server-status        (Status: 403) [Size: 301]                                   
===============================================================
2021/07/22 00:22:27 Finished
===============================================================
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Thu Jul 22 00:20:29 2021 as: nmap -sV -sC -oN nmap-initial 10.10.107.186
Nmap scan report for 10.10.107.186
Host is up (0.80s latency).
Not shown: 996 closed ports
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 90:35:66:f4:c6:d2:95:12:1b:e8:cd:de:aa:4e:03:23 (RSA)
|   256 53:9d:23:67:34:cf:0a:d5:5a:9a:11:74:bd:fd:de:71 (ECDSA)
|_  256 a2:8f:db:ae:9e:3d:c9:e6:a9:ca:03:b1:d7:1b:66:83 (ED25519)
80/tcp  open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Fowsniff Corp - Delivering Solutions
110/tcp open  pop3    Dovecot pop3d
|_pop3-capabilities: USER UIDL PIPELINING SASL(PLAIN) CAPA TOP RESP-CODES AUTH-RESP-CODE
143/tcp open  imap    Dovecot imapd
|_imap-capabilities: ENABLE have AUTH=PLAINA0001 IDLE more listed LOGIN-REFERRALS post-login capabilities LITERAL+ ID Pre-login SASL-IR OK IMAP4rev1
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jul 22 00:21:19 2021 -- 1 IP address (1 host up) scanned in 50.49 seconds
```
