---
title: "TryHackMe Advent of Cyber 2019 Day 6"
date: 2019-12-06
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2019"
event_day: "Day 6"
permalink: "/writeups/advent-of-cyber/adventofcyber-2019-day-6/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2019
  - day-6
---

# Data Elf-iltration

```text
export object > http
```

```text
christmaslists.zip has password to unzip
using john --> zip2john christmaslists.zip > for-john
	       john --wordlist /usr/share/wordlist/rockyou.txt for-john
password = [redacted]
uzip -> christmaslisttimmy.txt {answer 2}
```

```text
steghide extract -sf TryHackMe.jpg
christmasmonster.txt   {answer 3}
```

## Task

- What data was exfiltrated via DNS?
```text
Candy Cane Serial Number 8491   -via wireshark DNS
```

- What did Little Timmy want to be for Christmas?
```text
PenTester
```

- What was hidden within the file?
```text
RFC527
```
