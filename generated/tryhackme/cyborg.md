---
layout: writeup
title: "/cyborg"
permalink: "/writeups/tryhackme/cyborg/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Cyborg"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect cyborg</p>
  <h1>Cyborg</h1>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">2 docx note</span>
    <span class="tag">3 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Attack Path Overview</h2>
  <p>Cyborg usually combines web enumeration with Borg backup recovery: enumerate the exposed application, retrieve archive or configuration material, crack or reuse recovered credentials, gain a local shell, and finish with Linux privilege escalation.</p>
  <div class="tag-list">
    <span class="tag">web enumeration</span>
    <span class="tag">backup artifact recovery</span>
    <span class="tag">credential cracking</span>
    <span class="tag">Linux privesc</span>
  </div>
</section>

## Operator Notes

## Recon

- The exposed web paths reveal both administrative content and backup-related artifacts.
- The most valuable discovery is the Borg repository reference, which shifts the room from simple web enumeration into backup recovery.

## Initial Access

- The route to access is to extract the Borg archive with recovered credentials and mine the restored content for the next account secret.
- That recovered credential is then reused for SSH access to obtain the Linux foothold.

## Privilege Escalation

- After the SSH foothold, local enumeration drives the rest of the room.
- The box is designed to reward artifact analysis and credential recovery more than noisy exploitation.

## Defensive Takeaway

- Backup systems are highly sensitive because they frequently contain both data and operational secrets.
- Reusing credentials across backup tooling and user access paths multiplies the impact of a single leak.
- Publicly exposed administrative or backup content should be treated as a critical finding, not a misconfiguration footnote.

## Supporting Notes

### Secret

shoutout to all the people who have gotten to this stage whoop whoop!"

### Note

Wow I'm awful at remembering Passwords so I've taken my Friends advice and noting them down!
alex:S3cretP@s3

## Evidence Pack

### gobuster-initial

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.184.139
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/09/20 19:43:41 Starting gobuster in directory enumeration mode
===============================================================

/.htpasswd            (Status: 403) [Size: 278]

/.htaccess            (Status: 403) [Size: 278]

/.hta                 (Status: 403) [Size: 278]

/admin                (Status: 301) [Size: 314] [--> http://10.10.184.139/admin/]

/etc                  (Status: 301) [Size: 312] [--> http://10.10.184.139/etc/]  

/index.html           (Status: 200) [Size: 11321]                                

/server-status        (Status: 403) [Size: 278]                                  
===============================================================
2021/09/20 19:44:00 Finished
===============================================================
```

### .bash_logout

```text
# ~/.bash_logout: executed by bash(1) when login shell exits.

# when leaving the console clear the screen to increase privacy

if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q
fi
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Mon Sep 20 19:40:32 2021 as: nmap -sV -sC -oN nmap-initial -T3 10.10.184.139
Nmap scan report for 10.10.184.139
Host is up (0.24s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 db:b2:70:f3:07:ac:32:00:3f:81:b8:d0:3a:89:f3:65 (RSA)
|   256 68:e6:85:2f:69:65:5b:e7:c6:31:2c:8e:41:67:d7:ba (ECDSA)
|_  256 56:2c:79:92:ca:23:c3:91:49:35:fa:dd:69:7c:ca:ab (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Sep 20 19:41:00 2021 -- 1 IP address (1 host up) scanned in 28.01 seconds
```
