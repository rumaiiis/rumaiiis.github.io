---
title: "TryHackMe Advent of Cyber 2020 Day 13"
date: 2021-12-13
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2020"
event_day: "Day 13"
permalink: "/writeups/advent-of-cyber/25days-of-cybersecurity-day-13/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2020
  - day-13
---

# Aoc Day13

''''
nmap
22
23
111
''''

```text
login telnet
santa:clauschritmas

Ubuntu old version 12.04 have a keranl exploit

import dirty.c using python http.server

compile gcc -pthread dirty.c -o dirty -lcrypt  {got from source code from dirtycow}
and run ./dirty.c

created a new user with root privelege {firefart}
''''

# TASK

1. No answer needed

2. What old, deprecated protocol and service is runing?
```
Telnet
```text
3. What credentials was left for you?
```
clauschristmas
```text
4. What distribution of Linux and version number is this server running?
```
Ubuntu 12.04
```text
5. Who got here first?
```
Grinch
```text
6. NO answer

7. What is the verbatim syntax you can use to compile, taken from the real C source code comments?
```
gcc -pthread dirty.c -o dirty -lcrypt
```text
8. What "new" username was created, with the default operations of the real C source code?
```
firefart
```text
9. No answer needed

10. What is the MD5 hash output?
```
8b16f00dd3b51efadb02c1df7f8427cc
```text
=================================================
```
