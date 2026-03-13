---
layout: writeup
title: "/linuxenumeration"
permalink: "/writeups/tryhackme/linuxenumeration/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Linux Enumeration"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect linuxenumeration</p>
  <h1>Linux Enumeration</h1>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Workflow Focus</h2>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Operator Notes

## Recon

- This room follows the usual Linux boot-to-root pattern where service enumeration and artifact review reveal the access path.
- Linux Enumeration rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The initial foothold comes from exposed services, leaked files, or weak credentials rather than blind exploitation.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- Privilege escalation depends on local enumeration, trust abuse, writable automation, or delegated execution paths on the host.
- After the foothold, local context matters more than noisy exploitation.

## Defensive Takeaway

- The defensive lesson is that Linux post-exploitation paths are usually avoidable with better secret handling and tighter local permissions.
## Evidence Pack

### nmap-initial

```text
# Nmap 7.91 scan initiated Tue Jun 22 17:37:42 2021 as: nmap -sV -sC -A -oN nmap-initial 10.10.137.81
Nmap scan report for 10.10.137.81
Host is up (0.54s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 35:30:91:45:b9:d1:ed:5a:13:42:3e:20:95:6d:c7:b7 (RSA)
|   256 f5:69:6a:7b:c8:ac:89:b5:38:93:50:2f:05:24:22:70 (ECDSA)
|_  256 8f:4d:37:ba:40:12:05:fa:f0:e6:d6:82:fb:65:52:e8 (ED25519)
80/tcp   open  http    Apache httpd 2.4.29
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Index of /
3000/tcp open  http    PHP cli server 5.5 or later
|_http-title: Fox's website
Aggressive OS guesses: Linux 3.10 - 3.13 (95%), ASUS RT-N56U WAP (Linux 3.4) (95%), Linux 3.16 (95%), Linux 3.1 (93%), Linux 3.2 (93%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (92%), Linux 3.2 - 4.9 (92%), Linux 3.8 - 4.14 (92%), Linux 3.11 - 3.14 (92%), Synology DiskStation Manager 5.2-5644 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops
Service Info: Host: 127.0.1.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 554/tcp)
HOP RTT       ADDRESS
1   416.24 ms 10.2.0.1
2   ... 3
4   521.79 ms 10.10.137.81

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jun 22 17:40:18 2021 -- 1 IP address (1 host up) scanned in 157.92 seconds
```
