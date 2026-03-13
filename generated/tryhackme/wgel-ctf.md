---
layout: page
title: "/wgel-ctf"
permalink: "/writeups/tryhackme/wgel-ctf/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Wgel CTF"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect wgel-ctf</p>
  <h1>Wgel CTF</h1>
  <p>Linux room covering service enumeration, initial access, and privilege escalation. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">1 docx note</span>
    <span class="tag">5 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Wgel CTF is commonly approached through web directory discovery, username and SSH key recovery, access to a Linux user account, and local privilege escalation using misconfigured writable or executable paths.</p>
  <div class="tag-list">
    <span class="tag">directory enumeration</span>
    <span class="tag">SSH key discovery</span>
    <span class="tag">user shell</span>
    <span class="tag">Linux privesc</span>
  </div>
</section>

## Notes

## Recon

- Initial enumeration shows a simple Linux target, but the web content hides the real pivot inside the `sitemap` path.
- Further directory discovery inside that path exposes `.ssh` material and the user context needed for remote access.

## Initial Access

- The intended route is to recover the SSH private key associated with the exposed user and authenticate directly to the host.
- This turns content discovery into a full remote-login path without requiring password guessing.

## Privilege Escalation

- Local enumeration shows a permissive `sudo` rule for `wget`.
- That delegated binary can be abused to overwrite sensitive files or redirect privileged file operations, leading to root.

## Security Notes

- Publishing `.ssh` material under a web path is an immediate compromise condition, not a minor leakage issue.
- Key-based access is only stronger than passwords if the private key stays private.
- Even narrow `sudo` access to file-handling utilities like `wget` can be enough for full compromise.
## Collected Output

### gobuster-dirb-common-sitemap

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.143.129/sitemap/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/06/30 02:28:25 Starting gobuster in directory enumeration mode
===============================================================

/.htaccess            (Status: 403) [Size: 278]

/.ssh                 (Status: 301) [Size: 321] [--> http://10.10.143.129/sitemap/.ssh/]

/.htpasswd            (Status: 403) [Size: 278]                                         

/.hta                 (Status: 403) [Size: 278]                                         

/css                  (Status: 301) [Size: 320] [--> http://10.10.143.129/sitemap/css/] 

/fonts                (Status: 301) [Size: 322] [--> http://10.10.143.129/sitemap/fonts/]

/images               (Status: 301) [Size: 323] [--> http://10.10.143.129/sitemap/images/]

/index.html           (Status: 200) [Size: 21080]                                         

/js                   (Status: 301) [Size: 319] [--> http://10.10.143.129/sitemap/js/]    
===============================================================
2021/06/30 02:29:00 Finished
===============================================================
```

### gobuster-initial

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.143.129
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/06/30 02:09:00 Starting gobuster in directory enumeration mode
===============================================================

/sitemap              (Status: 301) [Size: 316] [--> http://10.10.143.129/sitemap/]

/server-status        (Status: 403) [Size: 278]
```

### gobuster-sitemap

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.143.129/sitemap/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/06/30 02:09:06 Starting gobuster in directory enumeration mode
===============================================================

/images               (Status: 301) [Size: 323] [--> http://10.10.143.129/sitemap/images/]

/css                  (Status: 301) [Size: 320] [--> http://10.10.143.129/sitemap/css/]   

/js                   (Status: 301) [Size: 319] [--> http://10.10.143.129/sitemap/js/]    

/fonts                (Status: 301) [Size: 322] [--> http://10.10.143.129/sitemap/fonts/] 

/sass                 (Status: 301) [Size: 321] [--> http://10.10.143.129/sitemap/sass/]
```

### nmap-full_port

```text
# Nmap 7.91 scan initiated Wed Jun 30 02:13:26 2021 as: nmap -p- -oN nmap-full_port -vv 10.10.143.129
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Wed Jun 30 02:02:36 2021 as: nmap -sV -sC -oN nmap-initial 10.10.143.129
Nmap scan report for 10.10.143.129
Host is up (0.49s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 94:96:1b:66:80:1b:76:48:68:2d:14:b5:9a:01:aa:aa (RSA)
|   256 18:f7:10:cc:5f:40:f6:cf:92:f8:69:16:e2:48:f4:38 (ECDSA)
|_  256 b9:0b:97:2e:45:9b:f3:2a:4b:11:c7:83:10:33:e0:ce (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jun 30 02:03:12 2021 -- 1 IP address (1 host up) scanned in 36.06 seconds
```
