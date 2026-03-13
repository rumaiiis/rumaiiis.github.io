---
layout: page
title: "/agentsudo"
permalink: "/writeups/tryhackme/agentsudo/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Agent Sudo"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect agentsudo</p>
  <h1>Agent Sudo</h1>
  <p>Linux room covering service enumeration, initial access, and privilege escalation. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">4 docx note</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Typical public walkthrough flow for this room is: enumerate HTTP/FTP/SSH, manipulate the User-Agent header to reveal the hidden clue, brute-force or recover FTP access for Chris, extract hidden material from the image files with binwalk and steghide, recover James's SSH access, then abuse sudo misconfiguration tied to CVE-2019-14287 for privilege escalation.</p>
  <div class="tag-list">
    <span class="tag">HTTP header manipulation</span>
    <span class="tag">FTP access recovery</span>
    <span class="tag">steganography workflow</span>
    <span class="tag">SSH foothold</span>
    <span class="tag">sudo CVE-2019-14287</span>
  </div>
</section>

## Notes

## Recon

- Initial enumeration exposes three primary services: `ftp`, `ssh`, and `http`.
- The web layer contains the first pivot. Changing the `User-Agent` value reveals the hidden clue path and points toward the next user context.

## Initial Access

- After identifying the hidden hint on the web service, the workflow moves to FTP access recovery.
- Image artifacts in the FTP-accessible material contain the next secrets. The intended path uses `binwalk` and `steghide`-style extraction to recover embedded data.
- Those recovered secrets provide the bridge to the SSH foothold.

## Privilege Escalation

- Once the Linux user shell is established, local enumeration shows a permissive `sudo` configuration.
- The escalation path maps to `CVE-2019-14287`, where a sudo rule can be abused to execute commands as root despite an apparent restriction.

## Security Notes

- Treat client-controlled headers as untrusted, but remember they can still expose workflow clues or logic differences during testing.
- Hidden data in images and archives is a common challenge pattern and a good reminder to inspect artifacts, not just obvious files.
- Sudo policy edge cases remain high-value privilege-escalation findings on Linux systems.

## Supporting Files

### To Agentj

Dear agent J,
All these alien like photos are fake! Agent R stored the real picture inside your directory. Your login password is somehow stored in the fake picture. It shouldn't be a problem for you.
From,
Agent C

### Message

Hi james,
Glad you find this message. Your login password is hackerrules!
Don't ask me why the password look cheesy, ask agent R who set this password for you.
Your buddy,
chris

## Collected Output

### nmap-initial

```text
# Nmap 7.91 scan initiated Wed Jun 23 22:58:18 2021 as: nmap -sV -sC -A -oN nmap-initial 10.10.39.230
Nmap scan report for 10.10.39.230
Host is up (0.50s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 ef:1f:5d:04:d4:77:95:06:60:72:ec:f0:58:f2:cc:07 (RSA)
|   256 5e:02:d1:9a:c4:e7:43:06:62:c1:9e:25:84:8a:e7:ea (ECDSA)
|_  256 2d:00:5c:b9:fd:a8:c8:d8:80:e3:92:4f:8b:4f:18:e2 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Announcement
Aggressive OS guesses: ASUS RT-N56U WAP (Linux 3.4) (95%), Linux 3.16 (95%), Linux 3.1 (93%), Linux 3.2 (93%), Linux 3.10 - 3.13 (93%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (92%), Synology DiskStation Manager 5.2-5644 (92%), Linux 3.8 (91%), QNAP QTS 4.0 - 4.2 (91%), Linux 2.6.32 - 3.10 (90%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 554/tcp)
HOP RTT       ADDRESS
1   412.32 ms 10.2.0.1
2   ... 3
4   554.03 ms 10.10.39.230

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jun 23 23:01:36 2021 -- 1 IP address (1 host up) scanned in 199.28 seconds
```
