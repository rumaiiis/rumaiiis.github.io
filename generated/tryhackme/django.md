---
layout: page
title: "/django"
permalink: "/writeups/tryhackme/django/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Django"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect django</p>
  <h1>Django</h1>
  <p>Web-focused room covering application testing, content discovery, and common attack paths. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Web and App Security</strong>.</p>
  <div class="tag-list">
    <span class="tag">Web and App Security</span>
    <span class="tag">1 docx note</span>
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
- Django rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The intended foothold comes from chaining application flaws, exposed content, or weak credentials into code execution or authenticated access.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- Once the app is compromised, the next step is to stabilize host access and enumerate for the final path to proof material.
- After the foothold, local context matters more than noisy exploitation.

## Security Notes

- The defensive lesson is that web compromise rarely stays in the web tier when secrets, upload paths, or admin functions are exposed.
## Collected Output

### nmap-initial

```text
# Nmap 7.91 scan initiated Fri Jun 18 20:50:52 2021 as: nmap -sV -sC -oN ./nmap-initial 10.10.213.1
Nmap scan report for 10.10.213.1
Host is up (0.50s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 35:30:91:45:b9:d1:ed:5a:13:42:3e:20:95:6d:c7:b7 (RSA)
|   256 f5:69:6a:7b:c8:ac:89:b5:38:93:50:2f:05:24:22:70 (ECDSA)
|_  256 8f:4d:37:ba:40:12:05:fa:f0:e6:d6:82:fb:65:52:e8 (ED25519)
8000/tcp open  http-alt WSGIServer/0.2 CPython/3.6.9
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 400 Bad Request
|     Date: Fri, 18 Jun 2021 15:21:26 GMT
|     Server: WSGIServer/0.2 CPython/3.6.9
|     Content-Type: text/html
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta http-equiv="content-type" content="text/html; charset=utf-8">
|     <meta name="robots" content="NONE,NOARCHIVE">
|     <title>DisallowedHost
|     /nice ports,/Trinity.txt.bak</title>
|     <style type="text/css">
|     html * { padding:0; margin:0; }
|     body * { padding:10px 20px; }
|     body * * { padding:0; }
|     body { font:small sans-serif; background-color:#fff; color:#000; }
|     body>div { border-bottom:1px solid #ddd; }
|     font-weight:normal; }
|     margin-bottom:.8em; }
|     margin:1em 0 .5em 0; }
|     margin:0 0 .5em 0; font-weight: normal; }
|     code, pre { font-size: 100%; white-space: pre-wrap; }
|     table { border:1px solid #ccc; border-collapse: collapse; width:100%; ba
|   GetRequest: 
|     HTTP/1.1 400 Bad Request
|     Date: Fri, 18 Jun 2021 15:21:18 GMT
|     Server: WSGIServer/0.2 CPython/3.6.9
|     Content-Type: text/html
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta http-equiv="content-type" content="text/html; charset=utf-8">
|     <meta name="robots" content="NONE,NOARCHIVE">
|     <title>DisallowedHost
|     /</title>
|     <style typ
```
