---
layout: writeup
title: "/mr-robot"
permalink: "/writeups/tryhackme/mr-robot/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Mr Robot"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect mr-robot</p>
  <h1>Mr Robot</h1>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">1 docx note</span>
    <span class="tag">2 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Attack Path Overview</h2>
  <p>Mr Robot is typically solved by enumerating the web root and hidden files, recovering credentials from site content, logging into WordPress, abusing plugin or theme execution for a shell, and escalating locally after stabilizing access.</p>
  <div class="tag-list">
    <span class="tag">content discovery</span>
    <span class="tag">credential recovery</span>
    <span class="tag">WordPress abuse</span>
    <span class="tag">shell stabilization</span>
    <span class="tag">Linux privesc</span>
  </div>
</section>

## Operator Notes

## Recon

- The web root leaks a large amount of content, and hidden files plus WordPress indicators quickly identify the application stack.
- Username enumeration is practical because the login flow responds differently to invalid usernames and invalid passwords.

## Initial Access

- The intended route is to recover the valid WordPress username, then work through the `fsocity.dic` credential source to recover the password.
- Once authenticated, theme or template editing provides a direct path to PHP code execution and a reverse shell.

## Privilege Escalation

- After landing on the host, the next credential pivot comes from the restricted user material stored locally.
- The final step uses a SUID-enabled `nmap` binary to jump from the user context to root.

## Defensive Takeaway

- Login error messages should never help an attacker separate valid usernames from invalid ones.
- Web application admin access must be treated as near-host compromise when file editing or code execution is available.
- Old SUID-enabled tooling remains a direct privilege-escalation path on Linux systems.
## Evidence Pack

### gobuster-initial

```text
/.hta                 (Status: 403) [Size: 213]

/.htaccess            (Status: 403) [Size: 218]

/.htpasswd            (Status: 403) [Size: 218]

/0                    (Status: 301) [Size: 0] [--> http://10.10.12.171/0/]

/admin                (Status: 301) [Size: 234] [--> http://10.10.12.171/admin/]

/audio                (Status: 301) [Size: 234] [--> http://10.10.12.171/audio/]

/atom                 (Status: 301) [Size: 0] [--> http://10.10.12.171/feed/atom/]

/blog                 (Status: 301) [Size: 233] [--> http://10.10.12.171/blog/]   

/css                  (Status: 301) [Size: 232] [--> http://10.10.12.171/css/]    

/dashboard            (Status: 302) [Size: 0] [--> http://10.10.12.171/wp-admin/] 

/favicon.ico          (Status: 200) [Size: 0]                                     

/feed                 (Status: 301) [Size: 0] [--> http://10.10.12.171/feed/]     

/images               (Status: 301) [Size: 235] [--> http://10.10.12.171/images/] 

/index.html           (Status: 200) [Size: 1188]                                  

/intro                (Status: 200) [Size: 516314]                                

/js                   (Status: 301) [Size: 231] [--> http://10.10.12.171/js/]
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Fri Jul  9 20:19:57 2021 as: nmap -sC -sV -oN nmap-initial 10.10.12.171
Nmap scan report for 10.10.12.171
Host is up (0.63s latency).
Not shown: 998 filtered ports
PORT    STATE  SERVICE  VERSION
22/tcp  closed ssh
443/tcp open   ssl/http Apache httpd
|_http-title: Site doesn't have a title (text/html).
| ssl-cert: Subject: commonName=www.example.com
| Not valid before: 2015-09-16T10:45:03
|_Not valid after:  2025-09-13T10:45:03

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jul  9 20:23:51 2021 -- 1 IP address (1 host up) scanned in 234.44 seconds
```
