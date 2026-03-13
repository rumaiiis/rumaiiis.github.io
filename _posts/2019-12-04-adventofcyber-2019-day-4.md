---
title: "TryHackMe Advent of Cyber 2019 Day 4"
date: 2019-12-04
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2019"
event_day: "Day 4"
permalink: "/writeups/advent-of-cyber/adventofcyber-2019-day-4/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2019
  - day-4
---

# Christmas Linux

```text
ssh
username: mcsysadmin
password: [redacted]
```

## Task

- How many visible files are there in the home directory(excluding ./ and ../)?
```text
8
```

- What is the content of file5?
```text
recipes
```

- Which file contains the string ‘password’?
```text
[redacted sensitive answer]
```

- What is the IP address in a file in the home folder?
```text
10.0.0.05               -via grep -Eo '[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}' *
```

- How many users can log into the machine?
```text
3
```

- What is the sha1 hash of file8?
```text
fa67ee594358d83becdd2cb6c466b25320fd2835
```

- What is mcsysadmin’s password hash?
```text
[redacted sensitive answer]
```
