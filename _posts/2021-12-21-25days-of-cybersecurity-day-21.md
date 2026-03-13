---
title: "TryHackMe Advent of Cyber 2020 Day 21"
date: 2021-12-21
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2020"
event_day: "Day 21"
permalink: "/writeups/advent-of-cyber/25days-of-cybersecurity-day-21/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2020
  - day-21
---

# AoC21

```text
10.10.72.63
```

```text
Remmina
littlehelper : iLove5now!
```

## Task

- Read the contents of the text file within the Documents folder. What is the file hash for db.exe?
```text
596690FFC54AB6101932856E6A78E3A1		-via get-content ./db file text.txt
```

- What is the file hash of the mysterious executable within the Documents folder?
```text
5F037501FB542AD2D9B06EB12AED09F0 		-via 	get-filehash -algorithm md5 ./deebee.exe
```

- Using Strings find the hidden flag within the executable?
```text
[redacted challenge flag]
```

- What is the flag that is displayed when you run the database connector file?
```text
[redacted challenge flag]
```
