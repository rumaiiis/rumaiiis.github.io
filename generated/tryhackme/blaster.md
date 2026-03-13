---
layout: page
title: "/blaster"
permalink: "/writeups/tryhackme/blaster/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Blaster"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect blaster</p>
  <h1>Blaster</h1>
  <p>Windows-focused room covering service enumeration, exploitation, and Active Directory concepts. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Windows and AD</strong>.</p>
  <div class="tag-list">
    <span class="tag">Windows and AD</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Windows-focused room covering service enumeration, exploitation, and Active Directory concepts. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Notes

## Recon

- Windows and domain-facing services are the core focus of this room, so careful service enumeration sets the direction early.
- Blaster rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The initial foothold usually comes from weak authentication, service abuse, or an exposed administrative surface on the Windows host.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- Privilege escalation depends on Windows post-exploitation, token context, or local service and task behavior.
- After the foothold, local context matters more than noisy exploitation.

## Security Notes

- The main lesson is that Windows management surfaces and legacy services must be hardened because one foothold often becomes full host control quickly.
## Collected Output

### initial-nmap

```text
# Nmap 7.91 scan initiated Tue Jun 15 15:12:24 2021 as: nmap -sC -sV --script vuln -Pn -oN initial-nmap 10.10.53.214
Nmap scan report for 10.10.53.214
Host is up (0.49s latency).
Not shown: 998 filtered ports
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-server-header: Microsoft-IIS/10.0
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_sslv2-drown: 
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jun 15 15:22:50 2021 -- 1 IP address (1 host up) scanned in 626.46 seconds
```
