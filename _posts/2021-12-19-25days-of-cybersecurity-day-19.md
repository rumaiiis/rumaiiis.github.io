---
title: "TryHackMe Advent of Cyber 2020 Day 19"
date: 2021-12-19
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2020"
event_day: "Day 19"
permalink: "/writeups/advent-of-cyber/25days-of-cybersecurity-day-19/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2020
  - day-19
---

# Naughty or Nice

```text
http://<ip>
after searching a name, noticing the url
http://10.10.64.227/?proxy=http%3A%2F%2Flist.hohoho%3A8080%2Fsearch.php%3Fname%3Drumais  -decode using cyber chef{url decoder}
http://10.10.64.227/?proxy=http://list.hohoho:8080/search.php?name=rumais
.hohoho is not a valid TLD

change url with
.localtest.me at the end of list.hohoho
got an hidden message for santa with password of admin
''''

# TASK

1. What is Santa's password?
```
Be good for goodness sake!
```text
2. What is the challenge flag?
```
THM{EVERYONE_GETS_PRESENTS}
```text
=============================
```
