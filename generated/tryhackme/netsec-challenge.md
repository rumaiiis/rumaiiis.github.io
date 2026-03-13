---
layout: page
title: "/netsec-challenge"
permalink: "/writeups/tryhackme/netsec-challenge/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Net Sec Challenge"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect netsec-challenge</p>
  <h1>Net Sec Challenge</h1>
  <p>Skill-building room covering reconnaissance, tooling, cracking, packet analysis, or security basics. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Recon and Fundamentals</strong>.</p>
  <div class="tag-list">
    <span class="tag">Recon and Fundamentals</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">2 docx note</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Skill-building room covering reconnaissance, tooling, cracking, packet analysis, or security basics. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Notes

## Recon

- This room is more about methodology than a single exploit, so the emphasis is on disciplined reconnaissance and tool use.
- Net Sec Challenge rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The useful progress comes from reading the environment correctly and validating the output of the relevant security tooling.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- If host access is part of the path, the post-exploitation steps are typically lightweight and focused on proof recovery rather than heavy exploitation.
- After the foothold, local context matters more than noisy exploitation.

## Security Notes

- The defensive lesson is that information exposure and weak operational practice often matter just as much as software vulnerabilities.

## Supporting Files

### Usernames

eddie
quinn

## Collected Output

### nmap-initial

```text
# Nmap 7.91 scan initiated Thu Oct 28 11:20:17 2021 as: nmap -sC -sV -oN nmap-initial -T4 10.10.228.155
Nmap scan report for 10.10.228.155
Host is up (0.77s latency).
Not shown: 995 closed ports
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         (protocol 2.0)
| fingerprint-strings: 
|   NULL: 
|_    SSH-2.0-OpenSSH_8.2p1 [redacted challenge flag]
| ssh-hostkey: 
|   3072 da:5f:69:e2:11:1f:7c:66:80:89:61:54:e8:7b:16:f3 (RSA)
|   256 3f:8c:09:46:ab:1c:df:d7:35:83:cf:6d:6e:17:7e:1c (ECDSA)
|_  256 ed:a9:3a:aa:4c:6b:16:e6:0d:43:75:46:fb:33:b2:29 (ED25519)
80/tcp   open  http        lighttpd
|_http-server-header: lighttpd [redacted challenge flag]
|_http-title: Hello, world!
139/tcp  open  netbios-ssn Samba smbd 4.6.2
445/tcp  open  netbios-ssn Samba smbd 4.6.2
8080/tcp open  http        Node.js (Express middleware)
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port22-TCP:V=7.91%I=7%D=10/28%Time=617A3A27%P=x86_64-pc-linux-gnu%r(NUL
SF:L,29,"SSH-2\.0-OpenSSH_8\.2p1\x20[redacted challenge flag]\r\n");

Host script results:
|_nbstat: NetBIOS name: NETSEC-CHALLENG, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2021-10-28T05:50:39
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Oct 28 11:20:45 2021 -- 1 IP address (1 host up) scanned in 28.07 seconds
```
