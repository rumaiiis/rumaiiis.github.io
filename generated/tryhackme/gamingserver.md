---
layout: writeup
title: "/gamingserver"
permalink: "/writeups/tryhackme/gamingserver/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Gaming Server"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect gamingserver</p>
  <h1>Gaming Server</h1>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">2 markdown source</span>
    <span class="tag">2 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Workflow Focus</h2>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Operator Notes

## Recon

- This room follows the usual Linux boot-to-root pattern where service enumeration and artifact review reveal the access path.
- Gaming Server rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The initial foothold comes from exposed services, leaked files, or weak credentials rather than blind exploitation.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- Privilege escalation depends on local enumeration, trust abuse, writable automation, or delegated execution paths on the host.
- After the foothold, local context matters more than noisy exploitation.

## Defensive Takeaway

- The defensive lesson is that Linux post-exploitation paths are usually avoidable with better secret handling and tighter local permissions.
## Evidence Pack

### gobuster-initial

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.117.156
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/07/05 20:50:08 Starting gobuster in directory enumeration mode
===============================================================

/.hta                 (Status: 403) [Size: 278]

/.htpasswd            (Status: 403) [Size: 278]

/.htaccess            (Status: 403) [Size: 278]

/index.html           (Status: 200) [Size: 2762]

/robots.txt           (Status: 200) [Size: 33]  

/secret               (Status: 301) [Size: 315] [--> http://10.10.117.156/secret/]

/server-status        (Status: 403) [Size: 278]                                   

/uploads              (Status: 301) [Size: 316] [--> http://10.10.117.156/uploads/]
===============================================================
2021/07/05 20:51:01 Finished
===============================================================
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Mon Jul  5 20:49:11 2021 as: nmap -sV -sC -oN nmap-initial 10.10.117.156
Nmap scan report for 10.10.117.156
Host is up (0.53s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 34:0e:fe:06:12:67:3e:a4:eb:ab:7a:c4:81:6d:fe:a9 (RSA)
|   256 49:61:1e:f4:52:6e:7b:29:98:db:30:2d:16:ed:f4:8b (ECDSA)
|_  256 b8:60:c4:5b:b7:b2:d0:23:a0:c7:56:59:5c:63:1e:c4 (ED25519)
80/tcp open  http    Apache/2.4.29 (Ubuntu)
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: House of danak
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jul  5 20:50:04 2021 -- 1 IP address (1 host up) scanned in 53.71 seconds
```
