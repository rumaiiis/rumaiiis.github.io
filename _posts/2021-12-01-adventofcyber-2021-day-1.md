---
title: "TryHackMe Advent of Cyber 2021 Day 1"
date: 2021-12-01
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2021"
event_day: "Day 1"
permalink: "/writeups/advent-of-cyber/adventofcyber-2021-day-1/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2021
  - day-1
---

# AdventOfCyber Day-1

```text
What is an IDOR vulnerability?
How do I find and exploit IDOR vulnerabilities?
```

```text
IDOR	Insecure Direct Object Reference
	Type of access control vulnerability
	occur when user supplied input to retrive data(files, data, documents) and too much trust placed on input data
```

```text
To find exploig

Query Component : this is passed in url whilw making a request
eg : http://website.cop/page?id=2
	here http:// - protocol
	     wesite.com - domain
	     id=2 - Query component
      this page potencially will showing us user personal information nad by change the id we could view deatils of another user.

Post Variable : Examine the content of forms on a website can sometimes reveal fields that could be vuolnerable

Coockie : to stay login and cookies are used to remember your session
	   Changing the value of this cookie could result in displaying another user's information.
```
