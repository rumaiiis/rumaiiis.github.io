---
layout: page
title: "/nerdherd"
permalink: "/writeups/tryhackme/nerdherd/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Nerd Herd"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect nerdherd</p>
  <h1>Nerd Herd</h1>
  <p>Linux room covering service enumeration, initial access, and privilege escalation. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">2 docx note</span>
    <span class="tag">3 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Nerd Herd is generally approached through layered clue-chaining: combine web hints, FTP artifacts, and SMB enumeration to recover credentials, obtain a Linux foothold, and then escalate through local weaknesses uncovered during post-exploitation.</p>
  <div class="tag-list">
    <span class="tag">multi-service enumeration</span>
    <span class="tag">cipher or clue analysis</span>
    <span class="tag">SMB credential recovery</span>
    <span class="tag">Linux post-exploitation</span>
  </div>
</section>

## Notes

## Recon

- This room expects the attacker to combine clues across web, FTP, and SMB instead of relying on a single service.
- The early hints come from source comments, encoded values, and leaked artifact names that only make sense after some decoding or pattern matching.

## Initial Access

- FTP and SMB enumeration provide the user context and the secret material needed to recover the working credentials.
- Once the share and clue chain are solved, SSH becomes the practical foothold into the Linux host.

## Privilege Escalation

- After login, local enumeration becomes the deciding factor.
- The final escalation depends on host weakness rather than application logic, and the room rewards thorough post-exploitation review.

## Security Notes

- Small clue leaks across multiple services often combine into a full credential path even if each single leak looks harmless.
- Shared secrets between SMB, FTP, and SSH reduce an attacker’s workload dramatically.
- Attackers only need one successful interpretation of a clue chain to turn soft exposure into root access.

## Supporting Files

### Hellon3Rd

all you need is in the leet

### Secr3T

Ssssh! don't tell this anyone because you deserved it this far:
check out "/this1sn0tadirect0ry"
Sincerely,
0xpr0N3rd
<3

## Collected Output

### gobuster-initial

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.29.89:1337/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/10/08 21:26:22 Starting gobuster in directory enumeration mode
===============================================================

/.htpasswd            (Status: 403) [Size: 278]

/.htaccess            (Status: 403) [Size: 278]

/admin                (Status: 301) [Size: 317] [--> http://10.10.29.89:1337/admin/]

/.hta                 (Status: 403) [Size: 278]                                     

/index.html           (Status: 200) [Size: 11755]                                   

/server-status        (Status: 403) [Size: 278]                                     
===============================================================
2021/10/08 21:27:12 Finished
===============================================================
```

### nmap-full-port

```text
# Nmap 7.91 scan initiated Fri Oct  8 21:12:04 2021 as: nmap -p- -sV -oN nmap-full-port -T4 -vvv 10.10.29.89
Increasing send delay for 10.10.29.89 from 0 to 5 due to 951 out of 2376 dropped probes since last increase.
Warning: 10.10.29.89 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.10.29.89
Host is up, received echo-reply ttl 63 (0.25s latency).
Scanned at 2021-10-08 21:12:05 IST for 2769s
Not shown: 65497 closed ports
Reason: 65497 resets
PORT      STATE    SERVICE     REASON         VERSION
21/tcp    open     ftp         syn-ack ttl 63 vsftpd 3.0.3
22/tcp    open     ssh         syn-ack ttl 63 OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
139/tcp   open     netbios-ssn syn-ack ttl 63 Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp   open     netbios-ssn syn-ack ttl 63 Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
1337/tcp  open     http        syn-ack ttl 63 Apache httpd 2.4.18 ((Ubuntu))
1374/tcp  filtered molly       no-response
3796/tcp  filtered spw-dialer  no-response
5089/tcp  filtered unknown     no-response
5668/tcp  filtered unknown     no-response
7016/tcp  filtered spg         no-response
10404/tcp filtered unknown     no-response
10512/tcp filtered unknown     no-response
11606/tcp filtered unknown     no-response
12539/tcp filtered unknown     no-response
13017/tcp filtered unknown     no-response
17486/tcp filtered unknown     no-response
18588/tcp filtered unknown     no-response
24260/tcp filtered unknown     no-response
24929/tcp filtered unknown     no-response
26976/tcp filtered unknown     no-response
28439/tcp filtered unknown     no-response
28510/tcp filtered unknown     no-response
29375/tcp filtered unknown     no-response
37443/tcp filtered unknown     no-response
38010/tcp filtered unknown     no-response
43314/tcp filtered unknown     no-response
44860/tcp filtered unknown     no-response
46321/tcp filtered unknown     no-response
48103/tcp filtered unknown     no-response
48107/tcp fi
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Fri Oct  8 20:00:54 2021 as: nmap -sC -sV -oN nmap-initial -T4 10.10.29.89
Nmap scan report for 10.10.29.89
Host is up (0.23s latency).
Not shown: 996 closed ports
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.8.224.214
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp  open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 0c:84:1b:36:b2:a2:e1:11:dd:6a:ef:42:7b:0d:bb:43 (RSA)
|   256 e2:5d:9e:e7:28:ea:d3:dd:d4:cc:20:86:a3:df:23:b8 (ECDSA)
|_  256 ec:be:23:7b:a9:4c:21:85:bc:a8:db:0e:7c:39:de:49 (ED25519)
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: NERDHERD; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -59m59s, deviation: 1h43m54s, median: 0s
|_nbstat: NetBIOS name: NERDHERD, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: nerdherd
|   NetBIOS computer name: NERDHERD\x00
|   Domain name: \x00
|   FQDN: nerdherd
|_  System time: 2021-10-08T17:31:29+03:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2021-10-08T14:31:29
|_  start_date: N/A

Servic
```
