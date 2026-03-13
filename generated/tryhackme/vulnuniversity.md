---
layout: page
title: "/vulnuniversity"
permalink: "/writeups/tryhackme/vulnuniversity/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "VulnUniversity"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect vulnuniversity</p>
  <h1>VulnUniversity</h1>
  <p>Web-focused room covering application testing, content discovery, and common attack paths. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Web and App Security</strong>.</p>
  <div class="tag-list">
    <span class="tag">Web and App Security</span>
    <span class="tag">2 docx note</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Web-focused room covering application testing, content discovery, and common attack paths. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Notes

## Recon

- The web application is the main attack surface, so content discovery, login behavior, and hidden paths matter immediately.
- VulnUniversity rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The intended foothold comes from chaining application flaws, exposed content, or weak credentials into code execution or authenticated access.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- Once the app is compromised, the next step is to stabilize host access and enumerate for the final path to proof material.
- After the foothold, local context matters more than noisy exploitation.

## Security Notes

- The defensive lesson is that web compromise rarely stays in the web tier when secrets, upload paths, or admin functions are exposed.

## Supporting Files

### Phpext

php
php2
php3
php4
phtml

## Collected Output

### nmap-initial

```text
# Nmap 7.91 scan initiated Thu Jun 17 10:23:44 2021 as: nmap --script vuln -sV -A -oN ./nmap-initial 10.10.64.249
Nmap scan report for 10.10.64.249
Host is up (0.44s latency).
Not shown: 994 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 3.0.3
|_sslv2-drown: 
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
3128/tcp open  http-proxy  Squid http proxy 3.5.12
|_http-server-header: squid/3.5.12
| vulners: 
|   cpe:/a:squid-cache:squid:3.5.12: 
|     	MSF:ILITIES/UBUNTU-CVE-2019-12525/	7.5	https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2019-12525/	*EXPLOIT*
|     	MSF:ILITIES/DEBIAN-CVE-2016-5408/	7.5	https://vulners.com/metasploit/MSF:ILITIES/DEBIAN-CVE-2016-5408/	*EXPLOIT*
|     	MSF:ILITIES/CENTOS_LINUX-CVE-2020-11945/	7.5	https://vulners.com/metasploit/MSF:ILITIES/CENTOS_LINUX-CVE-2020-11945/	*EXPLOIT*
|     	CVE-2020-11945	7.5	https://vulners.com/cve/CVE-2020-11945
|     	CVE-2019-12526	7.5	https://vulners.com/cve/CVE-2019-12526
|     	CVE-2019-12525	7.5	https://vulners.com/cve/CVE-2019-12525
|     	CVE-2019-12519	7.5	https://vulners.com/cve/CVE-2019-12519
|     	CVE-2016-3947	7.5	https://vulners.com/cve/CVE-2016-3947
|     	CVE-2020-24606	7.1	https://vulners.com/cve/CVE-2020-24606
|     	MSF:ILITIES/UBUNTU-CVE-2016-4052/	6.8	https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2016-4052/	*EXPLOIT*
|     	MSF:ILITIES/UBUNTU-CVE-2016-4051/	6.8	https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2016-4051/	*EXPLOIT*
|     	MSF:ILITIES/ORACLE_LINUX-CVE-2016-4052/	6.8	https://vulners.com/metasploit/MSF:ILITIES/ORACLE_LINUX-CVE-2016-4052/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP1-CVE-2016-4052/	6.8	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP1-CVE-2016-4052/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP1-CVE-2016-
```
