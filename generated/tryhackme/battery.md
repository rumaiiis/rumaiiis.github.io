---
layout: writeup
title: "/battery"
permalink: "/writeups/tryhackme/battery/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Battery"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect battery</p>
  <h1>Battery</h1>
  <p>General mixed challenge room blending enumeration, exploitation, and post-exploitation practice. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Challenge Labs</strong>.</p>
  <div class="tag-list">
    <span class="tag">Challenge Labs</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">2 docx note</span>
    <span class="tag">3 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Workflow Focus</h2>
  <p>General mixed challenge room blending enumeration, exploitation, and post-exploitation practice. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Operator Notes

## Recon

- The portal exposes a minimal web surface, but directory discovery reveals administrative and reporting paths that matter more than the landing page.
- The downloaded reporting artifact becomes the first real lead because it leaks usernames and hints about the application’s trust model.

## Initial Access

- The intended path centers on application logic flaws rather than brute force alone.
- By abusing inconsistent username-length handling between registration and login, the room can be approached as a truncation-style authentication issue.
- After gaining administrative access, the XML-processing functionality opens the door to XXE-based file reads and further credential discovery.

## Privilege Escalation

- Once higher-privileged credentials are recovered from application files and configuration data, the attack shifts into host access and local privilege escalation.
- The final step is less about a single public exploit and more about chaining the trust failures already present in the application stack.

## Defensive Takeaway

- Validation differences between registration and login paths can become authentication bypass conditions.
- XML parsers with unsafe external-entity handling turn ordinary features into file-read and secret-extraction primitives.
- Hardcoded credentials inside application files collapse the gap between web compromise and system compromise.

## Supporting Notes

### Emails

support@bank.a
contact@bank.a
cyber@bank.a
admins@bank.a
sam@bank.a
admin0@bank.a
super_user@bank.a
control_admin@bank.a
it_admin@bank.a

## Evidence Pack

### gobuster-initial

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.31.144/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/10/10 23:49:10 Starting gobuster in directory enumeration mode
===============================================================

/.htaccess            (Status: 403) [Size: 288]

/.htpasswd            (Status: 403) [Size: 288]

/.hta                 (Status: 403) [Size: 283]

/admin.php            (Status: 200) [Size: 663]

/index.html           (Status: 200) [Size: 406]

/report               (Status: 200) [Size: 16912]

/scripts              (Status: 301) [Size: 313] [--> http://10.10.31.144/scripts/]

/server-status        (Status: 403) [Size: 292]                                   
===============================================================
2021/10/10 23:49:30 Finished
===============================================================
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Sun Oct 10 23:48:11 2021 as: nmap -sV -sC -oN nmap-initial -T3 10.10.31.144
Nmap scan report for 10.10.31.144
Host is up (0.21s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 14:6b:67:4c:1e:89:eb:cd:47:a2:40:6f:5f:5c:8c:c2 (DSA)
|   2048 66:42:f7:91:e4:7b:c6:7e:47:17:c6:27:a7:bc:6e:73 (RSA)
|   256 a8:6a:92:ca:12:af:85:42:e4:9c:2b:0e:b5:fb:a8:8b (ECDSA)
|_  256 62:e4:a3:f6:c6:19:ad:30:0a:30:a1:eb:4a:d3:12:d3 (ED25519)
80/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Oct 10 23:48:35 2021 -- 1 IP address (1 host up) scanned in 24.20 seconds
```

### report

```text
ELF>@:@8@@@@hhhhmm   00-==hp-==DDPtdt"t"t"TTQtdRtd-==/lib64/ld-linux-x86-64.so.2GNUDh{t?NGNU

emk 92  #"__isoc99_scanfputsprintfsystem__cxa_finalizestrcmp__libc_start_mainlibc.so.6GLIBC_2.7GLIBC_2.2.5_ITM_deregisterTMCloneTable__gmon_start___ITM_registerTMCloneTableKii
Uui	_=p=0H@H@????	?
@ @(@0@8@
```
