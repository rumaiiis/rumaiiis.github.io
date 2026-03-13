---
layout: page
title: "/hackpark"
permalink: "/writeups/tryhackme/hackpark/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Hack Park"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect hackpark</p>
  <h1>Hack Park</h1>
  <p>Windows-focused room covering service enumeration, exploitation, and Active Directory concepts. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Windows and AD</strong>.</p>
  <div class="tag-list">
    <span class="tag">Windows and AD</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">2 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>HackPark typically revolves around the BlogEngine.NET surface: identify the vulnerable web application, gain code execution or a web shell through the application, then use Windows enumeration and scheduled-task or service abuse to reach administrative access.</p>
  <div class="tag-list">
    <span class="tag">ASP.NET application enumeration</span>
    <span class="tag">web shell delivery</span>
    <span class="tag">Windows enumeration</span>
    <span class="tag">task or service abuse</span>
  </div>
</section>

## Notes

## Recon

- The IIS-hosted web application is the main attack surface, and the login workflow is the first area to examine closely.
- BlogEngine.NET indicators and the administrative path make it clear that the box is built around application compromise rather than direct RDP abuse.

## Initial Access

- The room is commonly solved by recovering or brute-forcing the blog credentials and then abusing the vulnerable BlogEngine.NET path to execute code.
- That provides the initial Windows foothold and moves the workflow into system enumeration.

## Privilege Escalation

- Once on the host, the path to administrative access depends on Windows task or service behavior and artifact-driven enumeration.
- The room rewards stable shell management and careful Windows host review after the web compromise.

## Security Notes

- Web applications on Windows hosts collapse the gap between app compromise and system compromise when upload or code-execution features are exposed.
- Password quality still matters even when the final exploit chain relies on a specific application bug.
- Task and service hardening are critical because they often become the second-stage privilege-escalation path.
## Collected Output

### gobuster-initial

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.73.72/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/11/07 12:33:39 Starting gobuster in directory enumeration mode
===============================================================

/account              (Status: 301) [Size: 150] [--> http://10.10.73.72/account/]

/aspnet_client        (Status: 301) [Size: 156] [--> http://10.10.73.72/aspnet_client/]

/archives             (Status: 200) [Size: 8300]                                       

/archive              (Status: 200) [Size: 8299]                                       

/Archive              (Status: 200) [Size: 8299]                                       

/aux                  (Status: 500) [Size: 1763]                                       

/blog                 (Status: 500) [Size: 1208]                                       

/Blog                 (Status: 500) [Size: 1208]                                       

/Admin                (Status: 302) [Size: 171] [--> http://10.10.73.72/Account/login.aspx?ReturnURL=/Admin]

/admin                (Status: 302) [Size: 171] [--> http://10.10.73.72/Account/login.aspx?ReturnURL=/admin]

/ADMIN                (Status: 302) [Size: 171] [--> http://10.10.73.72/Account/login.aspx?ReturnURL=/ADMIN]

/com1                 (Status: 500) [Size: 1763]                                                            

/com2                 (Status: 500) [Size: 1763]                                                            

/com3                 (Status: 500) [Size: 1763]   
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Sun Nov  7 12:29:31 2021 as: nmap -sV -sC -Pn -T4 -oN nmap-initial -vv 10.10.73.72
Nmap scan report for 10.10.73.72
Host is up, received user-set (0.23s latency).
Scanned at 2021-11-07 12:29:35 IST for 35s
Not shown: 998 filtered ports
Reason: 998 no-responses
PORT     STATE SERVICE            REASON          VERSION
80/tcp   open  http               syn-ack ttl 124 Microsoft IIS httpd 8.5
| http-methods: 
|   Supported Methods: GET HEAD OPTIONS TRACE POST
|_  Potentially risky methods: TRACE
| http-robots.txt: 6 disallowed entries 
| /Account/*.* /search /search.aspx /error404.aspx 
|_/archive /archive.aspx
|_http-server-header: Microsoft-IIS/8.5
|_http-title: hackpark | hackpark amusements
3389/tcp open  ssl/ms-wbt-server? syn-ack ttl 124
| ssl-cert: Subject: commonName=hackpark
| Issuer: commonName=hackpark
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2021-11-06T06:58:19
| Not valid after:  2022-05-08T06:58:19
| MD5:   1ecc af84 7235 da33 3838 fcf9 4e58 cd2a
| SHA-1: 2271 0944 4058 b16b 64c5 0225 a2b3 776c 4fd7 810a
| -----BEGIN CERTIFICATE-----
| MIIC1DCCAbygAwIBAgIQVUAG/nUY6pNFTdJiyOWMqDANBgkqhkiG9w0BAQUFADAT
| MREwDwYDVQQDEwhoYWNrcGFyazAeFw0yMTExMDYwNjU4MTlaFw0yMjA1MDgwNjU4
| MTlaMBMxETAPBgNVBAMTCGhhY2twYXJrMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
| MIIBCgKCAQEA7zxkNuEjx4SzvXX8wMSfPhwOfUza5QilIBt2XQIqdua0LCrebzcg
| U0imWBxhw8rNDGa2xXUIG8imfJ3ljkj9MhJKjaN501y7N6czldFWDAeA3hjnwV/u
| SY+v/NqaQyPRqg5Iey7Cs700RrETSToqLKbPJkm2b9bnMq0UgeJEGF2KBakzp+Vq
| lZLFJZGHbfwcl+Ytl7/k1Z4ORFPxWnDwNI8cWzyO2ZBOlvd10KhOZ7HZ2EQvrmPq
| zRXMm2G/ynHNpXFzpuwXNNXJi0Qcj69wr3dP2Yb7FdRaS8J47yR4bxzvcNZF3C3t
| Fj1wuBGP1nEL12p1QYIXcggkysEDLIAyZQIDAQABoyQwIjATBgNVHSUEDDAKBggr
| BgEFBQcDATALBgNVHQ8EBAMCBDAwDQYJKoZIhvcNAQEFBQADggEBANfEjtc4XM29
| N7NaOuMansWeFD7PYvAC9XDkpWnNqDvJdymXaKcGKQEo/KuK4ksD3Fq8tgi91+n/
| QNBvJGLapn7Km0dODRtyoKBAjmPRuDHjKL2fnuJw+TKZdAfu8Auhryqxf3RSrDIY
| 5rdRuF7M/rC+9QB0AJ3wlvj0ep4miIlwtVy
```
