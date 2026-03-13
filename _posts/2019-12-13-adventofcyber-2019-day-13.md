---
title: "TryHackMe Advent of Cyber 2019 Day 13"
date: 2019-12-13
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2019"
event_day: "Day 13"
permalink: "/writeups/advent-of-cyber/adventofcyber-2019-day-13/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2019
  - day-13
---

# Blasterv1.1

nmap
```text
80
3389 ms-wbt-server Microsoft Terminal Services
```

```text
loking through the website got a comment with passowrd of wordpress login
wade:parzival
login wordpress
tried php reverse shell in Apperence> theme editor> archive.php
and run  http://10.10.125.44/retro/wp-content/themes/90s-retro/archive.php
but not worked
```

```text
login RDP using remmina
wade:parzival
--> user.txt
''''
```
priveleage escalation

```text
# TASK

1. A web server is running on the target. What is the hidden directory which the website lives on?
```
/retro    -via gobuster
```text
2. Gain initial access and read the contents of user.txt
```
THM{HACK_PLAYER_ONE}
```text
3. [Optional] Elevate privileges and read the content of root.txt
```
THM{COIN_OPERATATED_EXPLOITATION}
```text
====================================================
```
