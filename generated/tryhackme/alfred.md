---
layout: page
title: "/alfred"
permalink: "/writeups/tryhackme/alfred/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Alfred"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect alfred</p>
  <h1>Alfred</h1>
  <p>Windows-focused room covering service enumeration, exploitation, and Active Directory concepts. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Windows and AD</strong>.</p>
  <div class="tag-list">
    <span class="tag">Windows and AD</span>
    <span class="tag">1 docx note</span>
    <span class="tag">3 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Alfred is typically solved by identifying the exposed Jenkins service, abusing script-console or build functionality for code execution, establishing a Windows shell, and then using token or privilege abuse techniques to escalate to SYSTEM.</p>
  <div class="tag-list">
    <span class="tag">Jenkins enumeration</span>
    <span class="tag">authenticated code execution</span>
    <span class="tag">Windows shell access</span>
    <span class="tag">privilege escalation to SYSTEM</span>
  </div>
</section>

## Notes

## Recon

- Initial enumeration highlights two important web services: the default IIS site and a Jenkins instance on the alternate HTTP port.
- Jenkins is the true attack surface here, and the exposed service immediately suggests a CI/CD-driven compromise path rather than a classic Windows service exploit.

## Initial Access

- The practical route is to authenticate to Jenkins and abuse job execution or script-console style functionality to run commands on the host.
- That yields the first Windows shell and turns the room into a post-exploitation exercise.

## Privilege Escalation

- The escalation step relies on Windows token context and privilege abuse rather than a network exploit.
- Once the session is stabilized, the attacker can impersonate or leverage a higher-privileged token to reach `SYSTEM`.

## Security Notes

- CI/CD platforms are high-impact assets because build execution is effectively remote code execution by design.
- Alternate admin ports should be treated as core production exposure, not “secondary” services.
- Windows privilege token abuse is a reminder that post-exploitation hardening matters after the initial compromise.
## Collected Output

### nmap-fast

```text
# Nmap 7.91 scan initiated Tue Jun 22 10:23:43 2021 as: nmap -sS -sV -sC -T3 -Pn -oN nmap-fast 10.10.44.182
Nmap scan report for 10.10.44.182
Host is up (0.49s latency).
Not shown: 998 filtered ports
PORT     STATE SERVICE VERSION
80/tcp   open  http    Microsoft IIS httpd 7.5
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/7.5
|_http-title: Site doesn't have a title (text/html).
8080/tcp open  http    Jetty 9.4.z-SNAPSHOT
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Jetty(9.4.z-SNAPSHOT)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jun 22 10:26:46 2021 -- 1 IP address (1 host up) scanned in 182.74 seconds
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Tue Jun 22 09:52:24 2021 as: nmap -sV -sC -A -Pn -oN nmap-initial 10.10.44.182
Nmap scan report for 10.10.44.182
Host is up (0.45s latency).
Not shown: 997 filtered ports
PORT     STATE SERVICE    VERSION
80/tcp   open  http       Microsoft IIS httpd 7.5
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/7.5
|_http-title: Site doesn't have a title (text/html).
3389/tcp open  tcpwrapped
| ssl-cert: Subject: commonName=alfred
| Not valid before: 2021-06-21T04:21:49
|_Not valid after:  2021-12-21T04:21:49
8080/tcp open  http       Jetty 9.4.z-SNAPSHOT
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Jetty(9.4.z-SNAPSHOT)
|_http-title: Site doesn't have a title (text/html;charset=utf-8).
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|specialized|phone
Running (JUST GUESSING): Microsoft Windows 7|Vista|2008|8.1|Phone (88%)
OS CPE: cpe:/o:microsoft:windows_7 cpe:/o:microsoft:windows_vista::- cpe:/o:microsoft:windows_vista::sp1 cpe:/o:microsoft:windows_server_2008::sp1 cpe:/o:microsoft:windows_8 cpe:/o:microsoft:windows_8.1:r1 cpe:/o:microsoft:windows
Aggressive OS guesses: Microsoft Windows 7 (88%), Microsoft Windows Vista SP0 or SP1, Windows Server 2008 SP1, or Windows 7 (88%), Microsoft Windows Server 2008 R2 SP1 (87%), Microsoft Windows Server 2008 R2 or Windows 8 (87%), Microsoft Windows 7 SP1 (87%), Microsoft Windows 8.1 R1 (87%), Microsoft Windows Server 2008 R2 (86%), Microsoft Windows Server 2008 R2 SP1 or Windows 8 (86%), Microsoft Windows 7 Professional or Windows 8 (86%), Microsoft Windows 7 SP1 or Windows Server 2008 SP2 or 2008 R2 SP1 (86%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

TRACEROUTE (using port 3389/tcp)
HOP RTT       ADDRESS
1   318.34 ms 10.2.0.1
2   ... 3
4   451.15 ms 10.10.44.182

OS 
```
