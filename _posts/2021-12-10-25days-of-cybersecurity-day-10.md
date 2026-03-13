---
title: "TryHackMe Advent of Cyber 2020 Day 10"
date: 2021-12-10
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2020"
event_day: "Day 10"
permalink: "/writeups/advent-of-cyber/25days-of-cybersecurity-day-10/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2020
  - day-10
---

# aoc20cmnsmb

```text
SMB - Simple Message Block - "Natively supported by windows and not Linux"
NFS - Network File System - "Natively supported by Linux and not in Windows"
```

```text
enumerate samba usig enum4linux

enum4linux -S <ip>
- 3 users have shares
- here santa doesnot have a password to login
	smbclient //<ip>/tbfc-santa

''''

# TASK

1. Using enum4linux, how many users are there on the Samba server?
```
3		enum4linux -U <ip>
```text
2. Now how many shares are there on the Samba server?
```
4
```text
3. Use smbclient to try to login the share on Samba server. What share doesn't require a password?
```
tbfc-santa
```text
4. Log in to this share, what directory did ElfMcSkidy leave for Santa?
```
jingle-tunes
```text
=======================================================
```
