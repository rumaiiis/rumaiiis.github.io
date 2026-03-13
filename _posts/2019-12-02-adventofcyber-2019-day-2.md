---
title: "TryHackMe Advent of Cyber 2019 Day 2"
date: 2019-12-02
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2019"
event_day: "Day 2"
permalink: "/writeups/advent-of-cyber/adventofcyber-2019-day-2/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2019
  - day-2
---

# Christmas Challenge 2

```text
gobuster dir -u http://<ip>:3000 -w /usr/share/wordlist/dirb/commmon
```

## Task
- What is the path of hidden page?
```text
/sysadmin      -via gobuster
```

- What is the password you found?
```text
[redacted sensitive answer]
```

- What do you have to take to the 'partay'
```text
Eggnog         -via login in -> admin:[redacted]
```
