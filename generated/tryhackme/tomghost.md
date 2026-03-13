---
layout: page
title: "/tomghost"
permalink: "/writeups/tryhackme/tomghost/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Tomghost"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect tomghost</p>
  <h1>Tomghost</h1>
  <p>Linux room covering service enumeration, initial access, and privilege escalation. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">2 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Tomghost commonly begins with Tomcat and AJP enumeration. The usual path is to exploit the Ghostcat file-read issue, recover credential material from configuration files, pivot into SSH, and then escalate locally using accessible backup or key artifacts.</p>
  <div class="tag-list">
    <span class="tag">Tomcat enumeration</span>
    <span class="tag">Ghostcat or AJP abuse</span>
    <span class="tag">config-file credential recovery</span>
    <span class="tag">SSH pivot</span>
    <span class="tag">Linux privesc</span>
  </div>
</section>

## Notes

## Recon

- Service enumeration immediately highlights Tomcat and AJP, which is the real attack surface rather than the SSH service.
- The Tomcat version and exposed AJP port are the key indicators that the host is vulnerable to Ghostcat-style file disclosure.

## Initial Access

- The intended route is to abuse the AJP connector to read sensitive files from the Tomcat application context.
- Recovered credentials or key material are then reused to obtain SSH access and establish the Linux foothold.

## Privilege Escalation

- Once on the host, the room shifts into artifact-driven Linux escalation.
- Backup or private-key material left on disk provides the next pivot, and local trust relationships complete the final move to root.

## Security Notes

- AJP should not be exposed broadly, especially on older Tomcat deployments.
- Configuration and backup files often hold enough secrets to turn a file-read bug into full host access.
- Host cleanup matters: stale keys and archived materials remain dangerous long after the original service issue is patched.
## Collected Output

### gobuster-initial

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.199.240:8080
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/07/06 20:30:17 Starting gobuster in directory enumeration mode
===============================================================

/docs                 (Status: 302) [Size: 0] [--> /docs/]

/examples             (Status: 302) [Size: 0] [--> /examples/]

/favicon.ico          (Status: 200) [Size: 21630]             

/host-manager         (Status: 302) [Size: 0] [--> /host-manager/]

/manager              (Status: 302) [Size: 0] [--> /manager/]     
===============================================================
2021/07/06 20:31:00 Finished
===============================================================
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Tue Jul  6 20:26:32 2021 as: nmap -sV -sC -oN nmap-initial 10.10.199.240
Nmap scan report for 10.10.199.240
Host is up (0.59s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f3:c8:9f:0b:6a:c5:fe:95:54:0b:e9:e3:ba:93:db:7c (RSA)
|   256 dd:1a:09:f5:99:63:a3:43:0d:2d:90:d8:e3:e1:1f:b9 (ECDSA)
|_  256 48:d1:30:1b:38:6c:c6:53:ea:30:81:80:5d:0c:f1:05 (ED25519)
53/tcp   open  tcpwrapped
8009/tcp open  ajp13      Apache Jserv (Protocol v1.3)
| ajp-methods: 
|_  Supported methods: GET HEAD POST OPTIONS
8080/tcp open  http       Apache Tomcat 9.0.30
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/9.0.30
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jul  6 20:27:11 2021 -- 1 IP address (1 host up) scanned in 39.11 seconds
```
