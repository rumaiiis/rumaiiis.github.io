---
title: "TryHackMe Advent of Cyber 2020 Day 4"
date: 2021-12-04
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2020"
event_day: "Day 4"
permalink: "/writeups/advent-of-cyber/25days-of-cybersecurity-day-4/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2020
  - day-4
---

# DAY 4

''''
/api -via gobuster
site-log.php  -via /api
```text

```
wfuzz -c -z file,<wordlist> -u http://<ip>/api/site-log.php?date=FUZZ
got 20201125

flag in http://<ip>/api/sitelog.php?date=FUZZ
''''

## Task

- No answer

- Given the URL "http://shibes.xyz/api.php", what would the entire wfuzz command look like to query the "breed" parameter using the wordlist "big.txt" (assume that "big.txt" is in your current directory)
```text
wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ
```

- Use GoBuster (against the target you deployed -- not the shibes.xyz domain) to find the API directory. What file is there?
```text
site-log.php      -via gobuster found /api
```

- Fuzz the date parameter on the file you found in the API directory. What is the flag displayed in the correct post?
```text
[redacted challenge flag]
```
