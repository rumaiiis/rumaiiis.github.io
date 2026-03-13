---
layout: writeup
title: "/ice"
permalink: "/writeups/tryhackme/ice/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Ice"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect ice</p>
  <h1>Ice</h1>
  <p>Windows-focused room covering network service enumeration, exploitation, lateral movement concepts, or Active Directory workflow. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Windows and AD</strong>.</p>
  <div class="tag-list">
    <span class="tag">Windows and AD</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">2 docx note</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Attack Path Overview</h2>
  <p>Ice commonly follows a Metasploit-oriented Windows workflow: identify the vulnerable media service, exploit the target to gain a session, migrate or stabilize access, and complete post-exploitation with privilege-focused enumeration.</p>
  <div class="tag-list">
    <span class="tag">service fingerprinting</span>
    <span class="tag">Metasploit exploitation</span>
    <span class="tag">session management</span>
    <span class="tag">Windows post-exploitation</span>
  </div>
</section>

## Operator Notes

## Recon

- Service fingerprinting identifies the vulnerable media service and quickly points toward a known exploit path.
- This room is intentionally oriented toward exploit selection and Metasploit workflow rather than manual vulnerability development.

## Initial Access

- The intended route is to use the compatible exploit module to gain a session on the Windows host.
- After that initial compromise, session handling, migration, and stabilization become the main focus.

## Privilege Escalation

- Post-exploitation relies on Windows enumeration and session management rather than a separate complex exploit.
- The room emphasizes the operator workflow after compromise as much as the exploit itself.

## Defensive Takeaway

- Outdated desktop or media services can become remote access paths just as easily as server software.
- Exploitability matters, but so does what an attacker can do with the first session they obtain.
- Endpoint hardening and service minimization are still the simplest ways to reduce this type of exposure.

## Supporting Notes

### Sysytem Info

Host Name:                 DARK-PC
OS Name:                   Microsoft Windows 7 Professional
OS Version:                6.1.7601 Service Pack 1 Build 7601
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Workstation
OS Build Type:             Multiprocessor Free
Registered Owner:          Dark
Registered Organization:
Product ID:                00371-177-0000061-85305
Original Install Date:     11/12/2019, 4:48:23 PM
System Boot Time:          6/14/2021, 1:24:34 PM
System Manufacturer:       Xen
System Model:              HVM domU
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
[01]: Intel64 Family 6 Model 63 Stepping 2 GenuineIntel ~2394 Mhz
BIOS Version:              Xen 4.2.amazon, 8/24/2006
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume1
System Locale:             en-us;English (United States)
Input Locale:              en-us;English (United States)
Time Zone:                 (UTC-06:00) Central Time (US & Canada)
Total Physical Memory:     2,048 MB
Available Physical Memory: 1,483 MB
Virtual Memory: Max Size:  4,095 MB
Virtual Memory: Available: 3,461 MB
Virtual Memory: In Use:    634 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    WORKGROUP
Logon Server:              \\DARK-PC
Hotfix(s):                 2 Hotfix(s) Installed.
[01]: KB2534111
[02]: KB976902
Network Card(s):           1 NIC(s) Installed.
[01]: AWS PV Network Device
Connection Name: Local Area Connection 2
DHCP Enabled:    Yes
DHCP Server:     10.10.0.1
IP address(es)
[01]: 10.10.7.193
[02]: fe80::1bf:73a8:6254:51a8

## Evidence Pack

### initial-nmap

```text
# Nmap 7.91 scan initiated Mon Jun 14 23:57:07 2021 as: nmap -sC -sV --script vuln -oN initial-nmap 10.10.7.193
Nmap scan report for 10.10.7.193
Host is up (0.47s latency).
Not shown: 988 closed ports
PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  tcpwrapped
| rdp-vuln-ms12-020: 
|   VULNERABLE:
|   MS12-020 Remote Desktop Protocol Denial Of Service Vulnerability
|     State: VULNERABLE
|     IDs:  CVE:CVE-2012-0152
|     Risk factor: Medium  CVSSv2: 4.3 (MEDIUM) (AV:N/AC:M/Au:N/C:N/I:N/A:P)
|           Remote Desktop Protocol vulnerability that could allow remote attackers to cause a denial of service.
|           
|     Disclosure date: 2012-03-13
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0152
|       http://technet.microsoft.com/en-us/security/bulletin/ms12-020
|   
|   MS12-020 Remote Desktop Protocol Remote Code Execution Vulnerability
|     State: VULNERABLE
|     IDs:  CVE:CVE-2012-0002
|     Risk factor: High  CVSSv2: 9.3 (HIGH) (AV:N/AC:M/Au:N/C:C/I:C/A:C)
|           Remote Desktop Protocol vulnerability that could allow remote attackers to execute arbitrary code on the targeted system.
|           
|     Disclosure date: 2012-03-13
|     References:
|       http://technet.microsoft.com/en-us/security/bulletin/ms12-020
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0002
|_sslv2-drown: 
5357/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
8000/tcp  open  http         Icecast streaming media server
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-slowl
```
