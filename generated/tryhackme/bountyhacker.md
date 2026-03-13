---
layout: writeup
title: "/bountyhacker"
permalink: "/writeups/tryhackme/bountyhacker/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Bounty Hacker"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect bountyhacker</p>
  <h1>Bounty Hacker</h1>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">3 docx note</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Attack Path Overview</h2>
  <p>Public walkthroughs consistently solve Bounty Hacker by enumerating FTP, SSH, and HTTP, extracting a task list from exposed content, using the recovered wordlist against SSH, landing a low-privilege shell, and escalating with a sudo-allowed GTFOBins path.</p>
  <div class="tag-list">
    <span class="tag">multi-service enumeration</span>
    <span class="tag">artifact-based credential discovery</span>
    <span class="tag">SSH brute-force</span>
    <span class="tag">Linux privilege escalation</span>
  </div>
</section>

## Operator Notes

## Recon

- Initial enumeration exposes `ftp`, `ssh`, and `http`, which maps the room as a classic Linux multi-service target.
- Anonymous or weakly protected content on the exposed services leaks the task list and the first useful username context.

## Initial Access

- The recovered task list and password candidates point directly toward an SSH credential attack.
- The intended path is to validate the wordlist material against the user account and convert that into an SSH foothold.

## Privilege Escalation

- After landing the user shell, local enumeration reveals a sudo-allowed binary or command path that can be abused for escalation.
- The final step is a straightforward GTFOBins-style move from user to root.

## Defensive Takeaway

- Small operational notes can expose enough context to collapse the attacker’s enumeration time.
- Reused or weak credentials turn even a short wordlist into a practical remote-access path.
- Sudo delegation should always be reviewed with shell-escape paths in mind.

## Supporting Notes

### Locks

rEddrAGON
ReDdr4g0nSynd!cat3
Dr@gOn$yn9icat3
R3DDr46ONSYndIC@Te
ReddRA60N
R3dDrag0nSynd1c4te
dRa6oN5YNDiCATE
ReDDR4g0n5ynDIc4te
R3Dr4gOn2044
RedDr4gonSynd1cat3
R3dDRaG0Nsynd1c@T3
Synd1c4teDr@g0n
reddRAg0N
REddRaG0N5yNdIc47e
Dra6oN$yndIC@t3
4L1mi6H71StHeB357
rEDdragOn$ynd1c473
DrAgoN5ynD1cATE
ReDdrag0n$ynd1cate
Dr@gOn$yND1C4Te
RedDr@gonSyn9ic47e
REd$yNdIc47e
dr@goN5YNd1c@73
rEDdrAGOnSyNDiCat3
r3ddr@g0N
ReDSynd1ca7e

### Task

1.) Protect Vicious.
2.) Plan for Red Eye pickup on the moon.
-lin

## Evidence Pack

### nmap-initial

```text
# Nmap 7.91 scan initiated Thu Jun 24 15:36:58 2021 as: nmap -sV -sC -oN nmap-initial 10.10.178.83
Nmap scan report for 10.10.178.83
Host is up (0.52s latency).
Not shown: 967 filtered ports, 30 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
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
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 dc:f8:df:a7:a6:00:6d:18:b0:70:2b:a5:aa:a6:14:3e (RSA)
|   256 ec:c0:f2:d9:1e:6f:48:7d:38:9a:e3:bb:08:c4:0c:c9 (ECDSA)
|_  256 a4:1a:15:a5:d4:b1:cf:8f:16:50:3a:7d:d0:d8:13:c2 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jun 24 15:38:20 2021 -- 1 IP address (1 host up) scanned in 82.49 seconds
```
