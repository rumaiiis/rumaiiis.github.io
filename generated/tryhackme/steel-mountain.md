---
layout: page
title: "/steel-mountain"
permalink: "/writeups/tryhackme/steel-mountain/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Steel Mountain"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect steel-mountain</p>
  <h1>Steel Mountain</h1>
  <p>Windows-focused room covering service enumeration, exploitation, and Active Directory concepts. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Windows and AD</strong>.</p>
  <div class="tag-list">
    <span class="tag">Windows and AD</span>
    <span class="tag">1 docx note</span>
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
- Steel Mountain rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The initial foothold usually comes from weak authentication, service abuse, or an exposed administrative surface on the Windows host.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- Privilege escalation depends on Windows post-exploitation, token context, or local service and task behavior.
- After the foothold, local context matters more than noisy exploitation.

## Security Notes

- The main lesson is that Windows management surfaces and legacy services must be hardened because one foothold often becomes full host control quickly.
## Collected Output

### nmap-initial

```text
# Nmap 7.91 scan initiated Thu Jun 17 23:44:35 2021 as: nmap -sS -sV -sC -vv -Pn -oN ./nmap-initial 10.10.173.168
Increasing send delay for 10.10.173.168 from 0 to 5 due to 11 out of 24 dropped probes since last increase.
Nmap scan report for 10.10.173.168
Host is up, received user-set (0.68s latency).
Scanned at 2021-06-17 23:44:37 IST for 151s
Not shown: 988 closed ports
Reason: 988 resets
PORT      STATE SERVICE            REASON          VERSION
80/tcp    open  http               syn-ack ttl 125 Microsoft IIS httpd 8.5
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
|_http-server-header: Microsoft-IIS/8.5
|_http-title: Site doesn't have a title (text/html).
135/tcp   open  msrpc              syn-ack ttl 125 Microsoft Windows RPC
139/tcp   open  netbios-ssn        syn-ack ttl 125 Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       syn-ack ttl 125 Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
3389/tcp  open  ssl/ms-wbt-server? syn-ack ttl 125
| ssl-cert: Subject: commonName=steelmountain
| Issuer: commonName=steelmountain
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2021-06-16T18:13:04
| Not valid after:  2021-12-16T18:13:04
| MD5:   25c1 4c90 6175 ce2d 133e 21af 0099 ebcc
| SHA-1: 3d71 b3b0 b488 d867 277a 9929 5c81 42f8 5f2f a852
| -----BEGIN CERTIFICATE-----
| MIIC3jCCAcagAwIBAgIQdB+aGvPNIrFDijKnDlV6cjANBgkqhkiG9w0BAQUFADAY
| MRYwFAYDVQQDEw1zdGVlbG1vdW50YWluMB4XDTIxMDYxNjE4MTMwNFoXDTIxMTIx
| NjE4MTMwNFowGDEWMBQGA1UEAxMNc3RlZWxtb3VudGFpbjCCASIwDQYJKoZIhvcN
| AQEBBQADggEPADCCAQoCggEBAKk3UJkmvcr/JvT+YtQRbdOiYmABXzooFF7/drKW
| AIVX80nUgY45RF4YRHH/FbFh5ZGICfLSSAHI5GesV/zopS4s1l32hkD3wQ5UMQpL
| POZSXIMfr/ChdfsVHhpSPjqe7PEYhBDA9P7z1I/ZHjwXr6k+yhSmLK4vXY5J0yyc
| m838MA+5s751k5sd/o8uewHstkJ4Jq1u0g4NZx3estFR9uIS0qf8gjsVUOgjt5K7
| Yx049kZJI6Ccm6TVPtjakqvFwU9gWFpvyoIFhg87k5DPiMqXSMG+HUBX3E7OoQr3
| kRCNeiQ/coV+gODJdlK3tVf3X9AzFegcrJmtMobfBeng+iUCAwEAAaMkMCIwEwYD
| VR0lBAwwCgYIKwYB
```
