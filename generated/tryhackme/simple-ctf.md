---
layout: page
title: "/simple-ctf"
permalink: "/writeups/tryhackme/simple-ctf/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Simple CTF"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect simple-ctf</p>
  <h1>Simple CTF</h1>
  <p>Linux room covering service enumeration, initial access, and privilege escalation. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">2 docx note</span>
    <span class="tag">2 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Simple CTF generally involves standard Linux CTF methodology: enumerate web and SSH services, recover or brute-force credentials, obtain a foothold, and then escalate through locally exposed binaries, files, or sudo rights.</p>
  <div class="tag-list">
    <span class="tag">service enumeration</span>
    <span class="tag">credential recovery</span>
    <span class="tag">SSH foothold</span>
    <span class="tag">Linux privilege escalation</span>
  </div>
</section>

## Notes

## Recon

- The target exposes `ftp`, `http`, and `ssh` on a non-standard port.
- Directory enumeration on the web service identifies the `/simple` path, which points to the main application surface.
- Additional content discovery exposes the admin area and upload-related paths used during further testing.

## Initial Access

- The key application fingerprint is `CMS Made Simple`, and the room is commonly solved by validating the relevant SQL injection path against that version.
- Credential material recovered from the application and supporting files is then reused for SSH access.
- After the login succeeds, the low-privilege shell becomes the pivot for local enumeration.

## Privilege Escalation

- The local user has a useful `sudo` permission on `vim`.
- That leads to a direct `GTFOBins`-style escalation path and root shell access.

## Security Notes

- Directory enumeration still pays off against small CMS deployments because hidden admin panels and secondary paths often expose the real attack surface.
- Public CMS exploits become much more dangerous when paired with password reuse between the app and the operating system.
- Even narrow `sudo` allowances can become full compromise if the delegated binary supports shell escape.

## Supporting Files

### Formitch

Dammit man... you're the worst dev i've seen. You set the same pass for the system user, and the password is so weak... i cracked it in seconds. Gosh... what a mess!

## Collected Output

### nmap-initial

```text
# Nmap 7.91 scan initiated Tue Jun 22 06:31:55 2021 as: nmap -sV -sC -oN ./nmap-initial 10.10.134.10
Nmap scan report for 10.10.134.10
Host is up (0.52s latency).
Not shown: 997 filtered ports
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.2.54.48
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 2 disallowed entries 
|_/ /openemr-5_0_1_3 
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 29:42:69:14:9e:ca:d9:17:98:8c:27:72:3a:cd:a9:23 (RSA)
|   256 9b:d1:65:07:51:08:00:61:98:de:95:ed:3a:e3:81:1c (ECDSA)
|_  256 12:65:1b:61:cf:4d:e5:75:fe:f4:e8:d4:6e:10:2a:f6 (ED25519)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jun 22 06:33:13 2021 -- 1 IP address (1 host up) scanned in 77.76 seconds
```

### nmap-script

```text
# Nmap 7.91 scan initiated Tue Jun 22 06:40:17 2021 as: nmap -sV --script vuln -oN ./nmap-script 10.10.134.10
Nmap scan report for 10.10.134.10
Host is up (0.50s latency).
Not shown: 997 filtered ports
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
|_sslv2-drown: 
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-enum: 
|_  /robots.txt: Robots file
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| vulners: 
|   cpe:/a:apache:http_server:2.4.18: 
|     	CVE-2017-7679	7.5	https://vulners.com/cve/CVE-2017-7679
|     	CVE-2017-7668	7.5	https://vulners.com/cve/CVE-2017-7668
|     	CVE-2017-3169	7.5	https://vulners.com/cve/CVE-2017-3169
|     	CVE-2017-3167	7.5	https://vulners.com/cve/CVE-2017-3167
|     	MSF:ILITIES/REDHAT_LINUX-CVE-2019-0211/	7.2	https://vulners.com/metasploit/MSF:ILITIES/REDHAT_LINUX-CVE-2019-0211/	*EXPLOIT*
|     	MSF:ILITIES/IBM-HTTP_SERVER-CVE-2019-0211/	7.2	https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2019-0211/	*EXPLOIT*
|     	EXPLOITPACK:44C5118F831D55FAF4259C41D8BDA0AB	7.2	https://vulners.com/exploitpack/EXPLOITPACK:44C5118F831D55FAF4259C41D8BDA0AB	*EXPLOIT*
|     	CVE-2019-0211	7.2	https://vulners.com/cve/CVE-2019-0211
|     	1337DAY-ID-32502	7.2	https://vulners.com/zdt/1337DAY-ID-32502	*EXPLOIT*
|     	MSF:ILITIES/REDHAT_LINUX-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/REDHAT_LINUX-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/ORACLE-SOLARIS-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/ORACLE-SOLARIS-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/IBM-HTTP_SERVER-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP3-CVE-2018-1312/	6.8	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP3-CVE-
```
