---
title: "TryHackMe Advent of Cyber 2020 Day 2"
date: 2021-12-02
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2020"
event_day: "Day 2"
permalink: "/writeups/advent-of-cyber/25days-of-cybersecurity-day-2/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2020
  - day-2
---

# Elf Strikes Back

```text
For Elf McEager:
You have been assigned an ID number for your audit of the system: ODIzODI5MTNiYmYw . Use this to gain access to the upload section of the site.
Good luck!
```

## Task

- What string of text needs adding to the URL to get access to the upload page?
```text
/?id=ODIzODI5MTNiYmYw
```

- What type of file is accepted by the site?
```text
image           -via page source code
```

- In which directory are the uploaded files stored?
```text
/uploads/
```

- Activate your reverse shell and catch it in a netcat listener!
```text
no answer      -via upload php-reverse-shell with .jpeg.php extention
```

- What is the flag in /var/www/flag.txt?
```text
[redacted challenge flag]
```
