---
layout: writeup
title: "/startup"
permalink: "/writeups/tryhackme/startup/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Startup"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect startup</p>
  <h1>Startup</h1>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">3 docx note</span>
    <span class="tag">3 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Attack Path Overview</h2>
  <p>Startup is typically solved by enumerating FTP and web services, identifying an upload or writable-content path, obtaining a reverse shell, and then escalating through local credentials, scripts, or scheduled tasks left on the system.</p>
  <div class="tag-list">
    <span class="tag">FTP enumeration</span>
    <span class="tag">web content abuse</span>
    <span class="tag">reverse shell</span>
    <span class="tag">local escalation workflow</span>
  </div>
</section>

## Operator Notes

## Recon

- The box exposes a small service set, but anonymous FTP access and the mirrored web content make the writable file path the real priority.
- The `/files` area quickly becomes the central pivot because it links the FTP exposure to web-reachable content.

## Initial Access

- The intended path is to upload a web shell or command-capable payload through the writable FTP area and trigger it over HTTP.
- That provides the first host-level foothold without needing SSH credentials up front.

## Privilege Escalation

- During local enumeration, the packet capture becomes the source of the user credential, which moves the shell into a stronger user context.
- The final step depends on identifying a root-owned automation path and replacing or influencing the script it executes.

## Defensive Takeaway

- Anonymous writable FTP plus web-served content is effectively remote code execution waiting to happen.
- Internal network captures often leak much more than intended, including passwords and workflow clues.
- Root cron jobs should never execute user-controlled scripts or files.

## Supporting Notes

### .Test.Log

test

### Notice

Whoever is leaving these damn Among Us memes in this share, it IS NOT FUNNY. People downloading documents from our website will think we are a joke! Now I dont know who it is, but Maya is looking pretty sus.

## Evidence Pack

### gobuster-initial

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.225.18
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/09/29 20:21:24 Starting gobuster in directory enumeration mode
===============================================================

/.hta                 (Status: 403) [Size: 277]

/.htpasswd            (Status: 403) [Size: 277]

/.htaccess            (Status: 403) [Size: 277]

/files                (Status: 301) [Size: 312] [--> http://10.10.225.18/files/]

/index.html           (Status: 200) [Size: 808]                                 

/server-status        (Status: 403) [Size: 277]                                 
===============================================================
2021/09/29 20:21:46 Finished
===============================================================
```

### nmap-full-port

```text
# Nmap 7.91 scan initiated Wed Sep 29 20:27:20 2021 as: nmap -p- -vvv -oN nmap-full-port -T3 10.10.225.18
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Wed Sep 29 20:19:12 2021 as: nmap -sC -sV -oN nmap-initial -T3 10.10.225.18
Nmap scan report for 10.10.225.18
Host is up (0.36s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| drwxrwxrwx    2 65534    65534        4096 Nov 12  2020 ftp [NSE: writeable]
| -rw-r--r--    1 0        0          251631 Nov 12  2020 important.jpg
|_-rw-r--r--    1 0        0             208 Nov 12  2020 notice.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.8.224.214
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b9:a6:0b:84:1d:22:01:a4:01:30:48:43:61:2b:ab:94 (RSA)
|   256 ec:13:25:8c:18:20:36:e6:ce:91:0e:16:26:eb:a2:be (ECDSA)
|_  256 a2:ff:2a:72:81:aa:a2:9f:55:a4:dc:92:23:e6:b4:3f (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Maintenance
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Sep 29 20:19:37 2021 -- 1 IP address (1 host up) scanned in 25.53 seconds
```
