---
layout: page
title: "/attacktivedirectory"
permalink: "/writeups/tryhackme/attacktivedirectory/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Attacktive Directory"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect attacktivedirectory</p>
  <h1>Attacktive Directory</h1>
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
  <p>Attacktive Directory is usually solved as an AD enumeration and credential-abuse lab: identify the domain, enumerate valid users, discover AS-REP roastable accounts or sprayable credentials, pivot into SMB or remote-management access, and recover the domain proof material through standard Windows post-exploitation.</p>
  <div class="tag-list">
    <span class="tag">domain enumeration</span>
    <span class="tag">Kerberos user discovery</span>
    <span class="tag">AS-REP roasting or spraying</span>
    <span class="tag">SMB or remote access</span>
    <span class="tag">Windows post-exploitation</span>
  </div>
</section>

## Notes

## Recon

- This room is centered on Active Directory rather than a single host exploit, so the first step is domain and user enumeration.
- Kerberos, SMB, and other AD-facing services provide enough signal to identify the domain structure and likely attack paths.

## Initial Access

- The intended route is to enumerate valid users, identify weak credential opportunities, and abuse Kerberos-based weaknesses such as AS-REP roasting or password spraying.
- Once valid credentials are recovered, the room pivots into domain-aware access and proof collection.

## Privilege Escalation

- The privilege-escalation phase is more about expanding domain access and reading the right protected material than forcing a single exploit.
- Standard AD post-exploitation workflow and careful enumeration lead to the final flags.

## Security Notes

- User enumeration and Kerberos abuse remain highly effective against weakly hardened domains.
- Good password policy, pre-auth enforcement, and account monitoring materially reduce the success rate of these workflows.
- Small AD hygiene failures compound quickly because every recovered identity expands the attacker’s graph.
## Collected Output

### nmap-initial

```text
# Nmap 7.91 scan initiated Mon Jun 21 20:22:28 2021 as: nmap -sV -sC -oN ./nmap-initial 10.10.222.6
Nmap scan report for 10.10.222.6
Host is up (0.43s latency).
Not shown: 988 closed ports
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2021-06-21 14:53:48Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3269/tcp open  tcpwrapped
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=AttacktiveDirectory.spookysec.local
| Not valid before: 2021-06-20T14:52:08
|_Not valid after:  2021-12-20T14:52:08
|_ssl-date: 2021-06-21T14:54:27+00:00; +1s from scanner time.
Service Info: Host: ATTACKTIVEDIREC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2021-06-21T14:54:17
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jun 21 20:24:41 2021 -- 1 IP address (1 host up) scanned in 133.34 seconds
```
