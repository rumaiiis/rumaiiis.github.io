---
layout: writeup
title: "/blue"
permalink: "/writeups/tryhackme/blue/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Blue"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect blue</p>
  <h1>Blue</h1>
  <p>Windows-focused room covering network service enumeration, exploitation, lateral movement concepts, or Active Directory workflow. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Windows and AD</strong>.</p>
  <div class="tag-list">
    <span class="tag">Windows and AD</span>
    <span class="tag">1 docx note</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Attack Path Overview</h2>
  <p>Blue is generally solved by identifying legacy SMB exposure on Windows, validating the EternalBlue attack surface, gaining a shell through the SMB vulnerability path, and then performing standard post-exploitation to recover proof files and system-level access.</p>
  <div class="tag-list">
    <span class="tag">SMB enumeration</span>
    <span class="tag">EternalBlue</span>
    <span class="tag">Windows exploitation</span>
    <span class="tag">post-exploitation basics</span>
  </div>
</section>

## Operator Notes

## Recon

- The most important discovery is legacy SMB exposure on a Windows host with the right version profile for `MS17-010`.
- Vulnerability validation confirms that the box is built around the EternalBlue attack path.

## Initial Access

- The intended route is to exploit the SMB service and obtain a shell through the EternalBlue chain.
- Once code execution lands, the rest of the room shifts into straightforward Windows post-exploitation.

## Privilege Escalation

- The exploit itself effectively provides a high-privilege context, so the remaining work is to stabilize access and recover the proof material.
- The box is designed to teach the exploitation chain and the basic post-exploitation workflow that follows.

## Defensive Takeaway

- Legacy SMB exposure remains one of the clearest examples of how a single unpatched service can become full host compromise.
- Network segmentation and aggressive patching are still the most important defenses against exploit chains like EternalBlue.
- Even training boxes like this highlight why old Windows attack surface should be retired or isolated quickly.
## Evidence Pack

### initail-nmap

```text
# Nmap 7.91 scan initiated Mon Jun 14 17:57:07 2021 as: nmap -sC -sV --script vuln -oN initail-nmap 10.10.227.193
Nmap scan report for 10.10.227.193
Host is up (0.94s latency).
Not shown: 991 closed ports
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
|       http://technet.microsoft.com/en-us/security/bulletin/ms12-020
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0152
|   
|   MS12-020 Remote Desktop Protocol Remote Code Execution Vulnerability
|     State: VULNERABLE
|     IDs:  CVE:CVE-2012-0002
|     Risk factor: High  CVSSv2: 9.3 (HIGH) (AV:N/AC:M/Au:N/C:C/I:C/A:C)
|           Remote Desktop Protocol vulnerability that could allow remote attackers to execute arbitrary code on the targeted system.
|           
|     Disclosure date: 2012-03-13
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0002
|_      http://technet.microsoft.com/en-us/security/bulletin/ms12-020
|_ssl-ccs-injection: No reply from server (TIMEOUT)
|_sslv2-drown: 
49152/tcp open  unknown
49153/tcp open  unknown
49154/tcp open  unknown
49158/tcp open  unknown
49159/tcp open  unknown
Service Info: Host: JON-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED
|_smb-vuln-ms10-054: false
|_smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED
| smb-vuln-ms17-010: 
|   V
```
