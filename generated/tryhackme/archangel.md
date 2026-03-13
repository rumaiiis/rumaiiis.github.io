---
layout: page
title: "/archangel"
permalink: "/writeups/tryhackme/archangel/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Archangel"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect archangel</p>
  <h1>Archangel</h1>
  <p>Linux room covering service enumeration, initial access, and privilege escalation. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">1 docx note</span>
    <span class="tag">3 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Archangel generally follows an LFI-to-shell path: enumerate the hosted content, identify the local file inclusion issue, abuse log or file-based execution to gain code execution, then escalate through misconfigurations left on the Linux host.</p>
  <div class="tag-list">
    <span class="tag">directory enumeration</span>
    <span class="tag">LFI validation</span>
    <span class="tag">log poisoning or file execution</span>
    <span class="tag">Linux post-exploitation</span>
  </div>
</section>

## Notes

## Recon

- The initial web surface looks ordinary, but directory discovery and hostname clues quickly show that the interesting path sits behind secondary content.
- `robots.txt` and development-facing pages provide the first pivot toward the vulnerable application behavior.

## Initial Access

- The core issue is local file inclusion on the development PHP endpoint.
- After validating file read, the next step is to convert that inclusion path into code execution through a file- or log-based technique and then stabilize a shell.

## Privilege Escalation

- Once code execution is established, the room moves into Linux post-exploitation.
- The escalation route depends on local misconfiguration and execution context rather than a public kernel exploit.

## Security Notes

- Development pages and test endpoints are often the weakest link in otherwise small web stacks.
- LFI should never be treated as “just file read” because it often becomes shell access when paired with writable logs or scriptable inputs.
- Tight application separation and controlled execution paths reduce the blast radius after web compromise.
## Collected Output

### gobuster-dirbuster-list

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.95.41
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/06/30 21:55:50 Starting gobuster in directory enumeration mode
===============================================================

/images               (Status: 301) [Size: 311] [--> http://10.10.95.41/images/]

/flags                (Status: 301) [Size: 310] [--> http://10.10.95.41/flags/] 

/pages                (Status: 301) [Size: 310] [--> http://10.10.95.41/pages/] 

/layout               (Status: 301) [Size: 311] [--> http://10.10.95.41/layout/]
```

### gobuster-initial

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.95.41
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/06/30 21:48:20 Starting gobuster in directory enumeration mode
===============================================================

/.htaccess            (Status: 403) [Size: 276]

/.htpasswd            (Status: 403) [Size: 276]

/.hta                 (Status: 403) [Size: 276]

/flags                (Status: 301) [Size: 310] [--> http://10.10.95.41/flags/]

/images               (Status: 301) [Size: 311] [--> http://10.10.95.41/images/]

/index.html           (Status: 200) [Size: 19188]                               

/layout               (Status: 301) [Size: 311] [--> http://10.10.95.41/layout/]

/pages                (Status: 301) [Size: 310] [--> http://10.10.95.41/pages/] 

/server-status        (Status: 403) [Size: 276]                                 
===============================================================
2021/06/30 21:49:17 Finished
===============================================================
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Wed Jun 30 21:47:26 2021 as: nmap -sV -sC -oN nmap-initial 10.10.95.41
Nmap scan report for 10.10.95.41
Host is up (0.49s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9f:1d:2c:9d:6c:a4:0e:46:40:50:6f:ed:cf:1c:f3:8c (RSA)
|   256 63:73:27:c7:61:04:25:6a:08:70:7a:36:b2:f2:84:0d (ECDSA)
|_  256 b6:4e:d2:9c:37:85:d6:76:53:e8:c4:e0:48:1c:ae:6c (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Wavefire
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jun 30 21:49:17 2021 -- 1 IP address (1 host up) scanned in 111.30 seconds
```
