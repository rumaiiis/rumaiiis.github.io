---
layout: writeup
title: "/skynet"
permalink: "/writeups/tryhackme/skynet/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Skynet"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect skynet</p>
  <h1>Skynet</h1>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">4 docx note</span>
    <span class="tag">2 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Attack Path Overview</h2>
  <p>Skynet commonly combines SMB and web enumeration: discover accessible shares, recover credentials or hints, pivot through the application layer, gain shell access, and finish with a cron, script, or file-permission based privilege escalation path.</p>
  <div class="tag-list">
    <span class="tag">SMB enumeration</span>
    <span class="tag">credential discovery</span>
    <span class="tag">web pivot</span>
    <span class="tag">shell access</span>
    <span class="tag">Linux privesc</span>
  </div>
</section>

## Operator Notes

## Recon

- Enumeration shows a richer service set than a normal boot-to-root box, including SMB and mail-facing services alongside HTTP.
- SMB access and mail content provide the key sources of operational clues, usernames, and password material.

## Initial Access

- The common path is to recover or brute-force Miles Dyson’s mailbox access, harvest the hidden CMS path and related credentials, and then pivot through the web application.
- From there, file-inclusion style abuse against the application is used to land a reverse shell on the Linux host.

## Privilege Escalation

- After the user shell is established, the final step depends on local file permissions, writable scripts, or scheduled execution paths.
- The escalation route is more about chaining recovered access cleanly than forcing a single complex exploit.

## Defensive Takeaway

- Shared secrets across SMB, mail, and web services make multi-service environments much easier to break than they appear from outside.
- Hidden application paths are not protection; they only delay discovery until enumeration catches up.
- Internal scripts and automation need the same hardening attention as public-facing services.

## Supporting Notes

### Attention

A recent system malfunction has caused various passwords to be changed. All skynet employees are required to change their password after seeing this.
-Miles Dyson

### Important

- Add features to beta CMS /45kra24zxs28v3yd
- Work on T-800 Model 101 blueprints
- Spend more time with my wife

### Log1

cyborg007haloterminator
terminator22596
terminator219
terminator20
terminator1989
terminator1988
terminator168
terminator16
terminator143
terminator13
terminator123!@#
terminator1056
terminator101
terminator10
terminator02
terminator00
roboterminator
pongterminator
manasturcaluterminator
exterminator95
exterminator200
dterminator
djxterminator
dexterminator
determinator
cyborg007haloterminator
avsterminator
alonsoterminator
Walterminator
79terminator6
1996terminator

## Evidence Pack

### gobuster-initial

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.87.20
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/06/27 20:07:07 Starting gobuster in directory enumeration mode
===============================================================

/admin                (Status: 301) [Size: 310] [--> http://10.10.87.20/admin/]

/css                  (Status: 301) [Size: 308] [--> http://10.10.87.20/css/]  

/js                   (Status: 301) [Size: 307] [--> http://10.10.87.20/js/]   

/config               (Status: 301) [Size: 311] [--> http://10.10.87.20/config/]

/ai                   (Status: 301) [Size: 307] [--> http://10.10.87.20/ai/]    

/squirrelmail         (Status: 301) [Size: 317] [--> http://10.10.87.20/squirrelmail/]

/server-status        (Status: 403) [Size: 276]
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Sun Jun 20 09:06:07 2021 as: nmap -sS -sV -sC -vv -oN ./nmap-initial 10.10.254.189
Nmap scan report for 10.10.254.189
Host is up, received timestamp-reply ttl 61 (0.59s latency).
Scanned at 2021-06-20 09:06:08 IST for 44s
Not shown: 994 closed ports
Reason: 994 resets
PORT    STATE SERVICE     REASON         VERSION
22/tcp  open  ssh         syn-ack ttl 61 OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 99:23:31:bb:b1:e9:43:b7:56:94:4c:b9:e8:21:46:c5 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDKeTyrvAfbRB4onlz23fmgH5DPnSz07voOYaVMKPx5bT62zn7eZzecIVvfp5LBCetcOyiw2Yhocs0oO1/RZSqXlwTVzRNKzznG4WTPtkvD7ws/4tv2cAGy1lzRy9b+361HHIXT8GNteq2mU+boz3kdZiiZHIml4oSGhI+/+IuSMl5clB5/FzKJ+mfmu4MRS8iahHlTciFlCpmQvoQFTA5s2PyzDHM6XjDYH1N3Euhk4xz44Xpo1hUZnu+P975/GadIkhr/Y0N5Sev+Kgso241/v0GQ2lKrYz3RPgmNv93AIQ4t3i3P6qDnta/06bfYDSEEJXaON+A9SCpk2YSrj4A7
|   256 57:c0:75:02:71:2d:19:31:83:db:e4:fe:67:96:68:cf (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBI0UWS0x1ZsOGo510tgfVbNVhdE5LkzA4SWDW/5UjDumVQ7zIyWdstNAm+lkpZ23Iz3t8joaLcfs8nYCpMGa/xk=
|   256 46:fa:4e:fc:10:a5:4f:57:57:d0:6d:54:f6:c3:4d:fe (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICHVctcvlD2YZ4mLdmUlSwY8Ro0hCDMKGqZ2+DuI0KFQ
80/tcp  open  http        syn-ack ttl 61 Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Skynet
110/tcp open  pop3        syn-ack ttl 61 Dovecot pop3d
|_pop3-capabilities: CAPA TOP RESP-CODES PIPELINING UIDL AUTH-RESP-CODE SASL
139/tcp open  netbios-ssn syn-ack ttl 61 Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
143/tcp open  imap        syn-ack ttl 61 Dovecot imapd
|_imap-capabilities: ENABLE LOGINDISABLEDA0001 listed ID more LOGIN-REFERRALS have Pre-login capabilities SASL-IR post-login OK LITERAL+ IDLE IMAP4rev1
445/tcp open  netbios-ssn syn-ack ttl 61 Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
Se
```
