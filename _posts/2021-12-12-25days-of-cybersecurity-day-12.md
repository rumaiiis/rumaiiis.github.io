---
title: "TryHackMe Advent of Cyber 2020 Day 12"
date: 2021-12-12
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2020"
event_day: "Day 12"
permalink: "/writeups/advent-of-cyber/25days-of-cybersecurity-day-12/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2020
  - day-12
---

# aoc2cmnexp3 v1.1

```text
CGI - Common Gateway Interface
The commonplace for CGI scripts to be stored is within the /cgi-bin/ folder on webserver.
Take, for example, this systeminfo.sh file that displays the date, time and the user the webserver is running as:
	http://192.168.x.x/cgi-bin/systeminfo.sh

we could also run command like:
	http://x.x.x.x/cgi-bin/systeminfo.sh?&ls
	to list

on windows we can run systeminfo replacing ls to get usefull information
```

```text
To solve Elf McSkidy's problem with the elves slacking in the workshop, he has created the CGI script: elfwhacker.bat

Apache Tomcat/9.0.17 -- vulnerable

using metasploit {CVE-2019-0232}
set lost, rhosts, targeturi(/cgi-bin/elfwhacker.bak)
''''

# TASK

1. What is the the version numbrt of the web server?
```
9.0.17
```text
2. What CVE can be used to create a Meterpreter entry onto the machine?
```
CVE-2019-0232
```text
3. No answer needed

4. What is the contents of flag1.txt
```
thm{whacking_all_the_elves}
```text
5. No answer needed

==================================================
```
