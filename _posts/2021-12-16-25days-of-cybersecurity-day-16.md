---
title: "TryHackMe Advent of Cyber 2020 Day 16"
date: 2021-12-16
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2020"
event_day: "Day 16"
permalink: "/writeups/advent-of-cyber/25days-of-cybersecurity-day-16/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2020
  - day-16
---

# aoccmn 16

10.10.116.125

```text
nmap
80
22
```

```text
create a script find the hidden link
link-grabber.py
```

```text
crated a api key bruteforcing script
api-brute.py
```

## Task

- What is the port number for web server?
```text
80
```

- Without using enumerations tools such as Dirbuster, what is the directory for the API?  (without the API key)
```text
/api/
```

- Where is Santa right now?
```text
Winter Wonderland, Hyde Park, London.
```

- Find out the correct API key
```text
57
```
