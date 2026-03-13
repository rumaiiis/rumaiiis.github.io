---
layout: writeup
title: "/brooklyn-nine-nine"
permalink: "/writeups/tryhackme/brooklyn-nine-nine/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Brooklyn Nine-Nine"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect brooklyn-nine-nine</p>
  <h1>Brooklyn Nine-Nine</h1>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">1 docx note</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Attack Path Overview</h2>
  <p>Most walkthroughs for this room follow a lightweight Linux CTF path: enumerate FTP/SSH/HTTP, recover the note or credential hint, gain SSH access, check sudo rights, and escalate with the permitted binary through a GTFOBins-style technique.</p>
  <div class="tag-list">
    <span class="tag">FTP enumeration</span>
    <span class="tag">credential discovery</span>
    <span class="tag">SSH access</span>
    <span class="tag">sudo abuse</span>
  </div>
</section>

## Operator Notes

## Recon

- Brooklyn Nine-Nine is best approached through structured enumeration rather than noisy exploitation.
- The early workflow usually centers on FTP enumeration, credential discovery, which exposes the route into the room.

## Initial Access

- The intended foothold comes from following the attack path described in the room flow and validating the exposed service behavior.
- In practice, this means converting the discovered clues into working access through FTP enumeration and adjacent enumeration findings.

## Privilege Escalation

- After the first foothold, the room shifts into post-exploitation and local review.
- The key escalation themes are SSH access, sudo abuse, which complete the move to the final proof material.

## Defensive Takeaway

- Brooklyn Nine-Nine reinforces how small exposure points compound when enumeration is disciplined and service relationships are understood.
- The defensive lesson is to reduce credential reuse, remove unnecessary trust paths, and harden secondary services before they become the pivot.

## Supporting Notes

### Note To Jake

From Amy,
Jake please change your password. It is too weak and holt will be mad if someone hacks into the nine nine

## Evidence Pack

### nmap-initial

```text
# Nmap 7.91 scan initiated Mon Jul  5 20:16:21 2021 as: nmap -sV -sC -oN nmap-initial 10.10.46.132
Nmap scan report for 10.10.46.132
Host is up (3.5s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0             119 May 17  2020 note_to_jake.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.2.54.48
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 16:7f:2f:fe:0f:ba:98:77:7d:6d:3e:b6:25:72:c6:a3 (RSA)
|   256 2e:3b:61:59:4b:c4:29:b5:e8:58:39:6f:6f:e9:9b:ee (ECDSA)
|_  256 ab:16:2e:79:20:3c:9b:0a:01:9c:8c:44:26:01:58:04 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jul  5 20:17:25 2021 -- 1 IP address (1 host up) scanned in 63.74 seconds
```
