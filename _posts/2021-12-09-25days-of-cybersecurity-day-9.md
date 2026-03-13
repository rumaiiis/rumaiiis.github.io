---
title: "TryHackMe Advent of Cyber 2020 Day 9"
date: 2021-12-09
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2020"
event_day: "Day 9"
permalink: "/writeups/advent-of-cyber/25days-of-cybersecurity-day-9/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2020
  - day-9
---

# aoc2cmnftp

```text
FTP - File Transfer Protocol
FTP uses 2 connections

port 20  -  DATA
port 21  -  Commands
```

```text
ftp <ip>
anonymous login
after loging we got a .sh file
we changed the .sh file with nc reverse shell in pentest monkey
and put the edited .sh file replacing original

then set nc listerner in kali
we got reverse shell with root permission
```

## Task

- Name the directory on the FTP server that has data accessible by the "anonymous" user
```text
public
```

- What script gets executed within this directory?
```text
backup.sh
```

- What movie did Santa have on his Christmas shopping list?
```text
The Polar Express
```

- Re-upload this script to contain malicious data (just like we did in section 9.6. Output the contents of /root/flag.txt!
```text
[redacted challenge flag]
```
