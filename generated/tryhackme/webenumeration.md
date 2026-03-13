---
layout: writeup
title: "/webenumeration"
permalink: "/writeups/tryhackme/webenumeration/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Web Enumeration"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect webenumeration</p>
  <h1>Web Enumeration</h1>
  <p>Web-facing lab centered on application testing, content discovery, misconfiguration abuse, and foothold development. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Web and App Security</strong>.</p>
  <div class="tag-list">
    <span class="tag">Web and App Security</span>
    <span class="tag">1 docx note</span>
    <span class="tag">5 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Workflow Focus</h2>
  <p>Web-facing lab centered on application testing, content discovery, misconfiguration abuse, and foothold development. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Operator Notes

## Recon

- The web application is the main attack surface, so content discovery, login behavior, and hidden paths matter immediately.
- Web Enumeration rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The intended foothold comes from chaining application flaws, exposed content, or weak credentials into code execution or authenticated access.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- Once the app is compromised, the next step is to stabilize host access and enumerate for the final path to proof material.
- After the foothold, local context matters more than noisy exploitation.

## Defensive Takeaway

- The defensive lesson is that web compromise rarely stays in the web tier when secrets, upload paths, or admin functions are exposed.
## Evidence Pack

### gobuster-changes-dir

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.89.152/Changes
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt,html,conf,config,php
[+] Timeout:                 10s
===============================================================
2021/06/27 11:25:55 Starting gobuster in directory enumeration mode
===============================================================

/changes.conf         (Status: 200) [Size: 24]
```

### gobuster-dir

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.89.152
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/06/27 11:18:36 Starting gobuster in directory enumeration mode
===============================================================

/images               (Status: 301) [Size: 313] [--> http://10.10.89.152/images/]

/public               (Status: 301) [Size: 313] [--> http://10.10.89.152/public/]

/css                  (Status: 301) [Size: 310] [--> http://10.10.89.152/css/]   

/js                   (Status: 301) [Size: 309] [--> http://10.10.89.152/js/]    

/Changes              (Status: 301) [Size: 314] [--> http://10.10.89.152/Changes/]

/VIDEO                (Status: 301) [Size: 312] [--> http://10.10.89.152/VIDEO/]
```

### gobuster-vhost

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:          http://webenum.thm
[+] Method:       GET
[+] Threads:      64
[+] Wordlist:     /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt
[+] User Agent:   gobuster/3.1.0
[+] Timeout:      10s
===============================================================
2021/06/27 11:44:26 Starting gobuster in VHOST enumeration mode
===============================================================

Found: learning.webenum.thm (Status: 200) [Size: 13245]

Found: products.webenum.thm (Status: 200) [Size: 4941]
```

### wpscan-plugin

```text
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.18
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[32m[+][0m URL: http://wpscan.thm/ [10.10.44.105]
[32m[+][0m Started: Sun Jun 27 13:15:44 2021

Interesting Finding(s):

[32m[+][0m Headers
 | Interesting Entry: Server: Apache/2.4.29 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[32m[+][0m XML-RPC seems to be enabled: http://wpscan.thm/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[32m[+][0m WordPress readme found: http://wpscan.thm/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[32m[+][0m The external WP-Cron seems to be enabled: http://wpscan.thm/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[32m[+][0m WordPress version 5.0 identified (Insecure, released on 2018-12-06).
 | Found By: Rss Generator (Passive Detection)
```

### wpscan-theme

```text
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.18
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[32m[+][0m URL: http://wpscan.thm/ [10.10.44.105]
[32m[+][0m Started: Sun Jun 27 13:12:54 2021

Interesting Finding(s):

[32m[+][0m Headers
 | Interesting Entry: Server: Apache/2.4.29 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[32m[+][0m XML-RPC seems to be enabled: http://wpscan.thm/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[32m[+][0m WordPress readme found: http://wpscan.thm/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[32m[+][0m The external WP-Cron seems to be enabled: http://wpscan.thm/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[32m[+][0m WordPress version 5.0 identified (Insecure, released on 2018-12-06).
 | Found By: Rss Generator (Passive Detection)
```
