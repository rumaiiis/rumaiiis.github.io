---
layout: page
title: "/bolt"
permalink: "/writeups/tryhackme/bolt/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Bolt"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect bolt</p>
  <h1>Bolt</h1>
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
  <p>Bolt commonly follows a lightweight CMS attack path: fingerprint the Bolt CMS instance, recover or brute-force valid access, abuse administrative functionality to obtain code execution, and then stabilize a shell on the Linux host.</p>
  <div class="tag-list">
    <span class="tag">CMS fingerprinting</span>
    <span class="tag">credential recovery</span>
    <span class="tag">admin-panel abuse</span>
    <span class="tag">Linux foothold</span>
  </div>
</section>

## Notes

## Recon

- Service enumeration shows the normal web front and a second web service where the actual CMS is hosted.
- CMS fingerprinting quickly identifies Bolt and gives both the version context and the likely administrative attack surface.

## Initial Access

- The practical path is to recover or validate the exposed CMS credentials and log into the administrative interface.
- From there, the challenge pivots into authenticated remote code execution through the Bolt application rather than a public unauthenticated exploit path.

## Privilege Escalation

- Once code execution is available through the CMS, the remaining work is to stabilize the Linux shell and enumerate locally for proof material.
- The room emphasizes web-to-host compromise more than a separate complex root exploit.

## Security Notes

- Secondary application ports are often more important than the default website and should not be treated as less sensitive.
- CMS administrator access is already high-impact; patch lag and credential reuse make it even worse.
- Application admins should be isolated from operating-system trust wherever possible.
## Collected Output

### nmap-initial

```text
# Nmap 7.91 scan initiated Tue Jun 22 20:46:29 2021 as: nmap -sV -sC -A -oN nmap-initial 10.10.131.238
Nmap scan report for 10.10.131.238
Host is up (0.43s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f3:85:ec:54:f2:01:b1:94:40:de:42:e8:21:97:20:80 (RSA)
|   256 77:c7:c1:ae:31:41:21:e4:93:0e:9a:dd:0b:29:e1:ff (ECDSA)
|_  256 07:05:43:46:9d:b2:3e:f0:4d:69:67:e4:91:d3:d3:7f (ED25519)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
8000/tcp open  http    (PHP 7.2.32-1)
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 404 Not Found
|     Date: Tue, 22 Jun 2021 15:18:50 GMT
|     Connection: close
|     X-Powered-By: PHP/7.2.32-1+ubuntu18.04.1+deb.sury.org+1
|     Cache-Control: private, must-revalidate
|     Date: Tue, 22 Jun 2021 15:18:50 GMT
|     Content-Type: text/html; charset=UTF-8
|     pragma: no-cache
|     expires: -1
|     X-Debug-Token: 61a989
|     <!doctype html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">
|     <title>Bolt | A hero is unleashed</title>
|     <link href="https://fonts.googleapis.com/css?family=Bitter|Roboto:400,400i,700" rel="stylesheet">
|     <link rel="stylesheet" href="/theme/base-2018/css/bulma.css?8ca0842ebb">
|     <link rel="stylesheet" href="/theme/base-2018/css/theme.css?6cb66bfe9f">
|     <meta name="generator" content="Bolt">
|     </head>
|     <body>
|     href="#main-content" class="vis
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Date: Tue, 22 Jun 2021 15:18:48 GMT
|     Connection: close
|     X-Powered-By: PHP/7.2.32-1+ubuntu18.04.1+deb.sury.org+1
|     Cache-Control: public, s-maxage=600
|     Date: Tue, 22 Jun 2021 15:18:48 GMT
|     Content-Type: text/html; charset=UTF-8
|     
```
