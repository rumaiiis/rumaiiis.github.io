---
layout: page
title: "/notes"
permalink: "/writeups/tryhackme/notes/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Notes"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect notes</p>
  <h1>Notes</h1>
  <p>Mixed challenge room covering enumeration, exploitation, and post-exploitation practice. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Challenge Labs</strong>.</p>
  <div class="tag-list">
    <span class="tag">Challenge Labs</span>
    <span class="tag">5 docx note</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Mixed challenge room covering enumeration, exploitation, and post-exploitation practice. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Notes

## Recon

- This room mixes discovery, analysis, and exploitation, so the right path usually appears only after multiple clues are combined.
- Notes rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- Initial access depends on linking those clues together rather than relying on a single obvious vulnerability.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- After the foothold, the room transitions into standard host enumeration and local privilege-escalation review.
- After the foothold, local context matters more than noisy exploitation.

## Security Notes

- The defensive lesson is that seemingly minor leaks across different services often combine into full compromise when an attacker is systematic.

## Supporting Files

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

### Error Code

common errror codes:
100-199: Information
200-299: Successes (200 OK is the "normal" response for a GET)
300-399: Redirects (the information you want is elsewhere)
400-499: Client errors (You did something wrong, like asking for something that doesn't exist)
500-599: Server errors (The server tried, but something went wrong on their side)

### Nmap Cheatsheet

## nmap cheatsheet
********switches***********
-sS = syn scan  [-sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans]
-sU = UDP scan
-O  = detect operating system
-sV = detect the version of the services running
-A  = Aggrisive [activates service detection, operating system detection, a traceroute and common script scanning]
-T<1-5> = speed scan [more speed chance of error]
-p- = scan all ports
-sn = ping sweep [sends ping request to all of the possisible ip in network "nmap -sn 192.168.10.0/24"]
-oA = save in 2 format
-oN = save in normal format
-oG = save in grepable format
**********************************************
3 basic scan type:
-sT = TCP scan
-sS = SYN [half open]
-sU = UDP scan [take more time to scan so use "nmap -sU --top-ports 20 <target>"]
firewall evasion:          [he target host should respond with a RST if the port is closed]
-sN = NULL [when the TCP request is sent with no flags set at all.]
-sF = FIN [sent with the FIN flag ]
-sX = Xmas [PSH, URG and FIN]
nmap scritps stored in /usr/share/nmap/scripts
*******ports******
65535 available ports
1024 well-known ports
80 = http
443 = https
139 = Windows NETBIOS
445 = SMB
21  = FTP

### Stable Shell

python
---------{work on linux because linux come with buildin pthton}
if any version of python installed we can use :
python -c 'import pty;pty.spawn("/bin/bash")'
export TERM=xterm -- this will give us access to term commands such as clear.
rlwrap
--------{perticularly applicable in windows}
To use rlwrap, we invoke a slightly different listener:
before apt install rlwrap
rlwrap nc -lvnp <port>

### Xxs Note

Cross Site Script {XSSR}
this is a type of inject where attacker can execute malicios script on victims machine.
caused by unsanitized user input, in Javascript, VBscript, Flash, CSS.
Two categories : persistent/store and reflected.
attacks :
-Stealing Cookie {this contain authenticated session, attacker can login withot authentication}
-Keyloggging
-Webcam snapshot
-phishing
-port scaning
-Other browser based exploits. {millions possisible actually}
Stored XSS {most dangerous}
***************************
occured because unsanitized input field in code.
steps:
1)attacker inserts malicious payload in wesite database.        --attacker
2)for everey visit in wesite the malicious script in activated. --server
3)could steal victims cookie to takeover clients.--victims
Reflected XSS
*************
an attacker needs to trick a victim into clicking a URL to execute their malicious payload.
Reflected XSS is the most common type of XSS attack
steps:
1)send malicious payload to victim
2)once click link, the link execute script in website
3)data attacker gathered send back to him. They could steal the cookie also which results take down of vivtims a/c.
prevent XSS :
Escaping - Escape all user input.  means any data your application has received  is secure before rendering it for your end users.
{you could disallow the < and > characters from being rendered.}
Validating Input - Input validation is disallowing certain characters from being submit in the first place.
Sanitising - {strong method} for example you could sanitise the < character into the HTML entity &#60;
