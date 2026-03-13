---
title: "TryHackMe Advent of Cyber 2020 Day 24"
date: 2021-12-24
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2020"
event_day: "Day 24"
permalink: "/writeups/advent-of-cyber/25days-of-cybersecurity-day-24/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2020
  - day-24
---

# Light Cycle

```text
10.10.191.140
```

nmap
```text
80	http
65000	http
```

```text
gobuster in port 65000
/uploads.php
/grid
```

```text
bypassing the uploads.php page with php reverse shell

to remove client side filter we intercept the request by removing the javascript in intercept client request option,
then drop the js filter page

know to bypass server side filter we add .jpeg.php entention
then the php reverse shell is uploaded

run the reverse shell in /grid
```

```text
got username and password in /var/www/TheGrid/includes/dbauth.php
tron : IFightForTheUsers

mysql -utron -p
IFifgtForTheUsers

in mysql found username:[redacted]
flynn : edc621628f6d19a13a00fd683f5e3ff7

cracking hash-password =[redacted] [redacted]
```

```text
switch to fynn
su - flynn

user is in lxd group
we can exploit this to get root { reference Hacking Article }
```

## Task

- SCan the machine. What ports are open?
```text
80, 65000
```

- What's the title of the hidden website? It's worthwhile looking recursively at all websites on the box for this step.
```text
Light Cycle
```

- What is the name of the hidden php page?
```text
uploads.php
```

- What is the name of the hidden directory where file uploads are saved?
```text
grid
```

- Bypass the filters. Upload and execute a reverse shell.
```text
no answer needed
```

- What is the value of the web.txt flag?
```text
[redacted challenge flag]
```

- Upgrade and stabilize your shell.
```text
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

- Review the configuration files for the webserver to find some useful loot in the form of credentials. What credentials do you find? username:[redacted]
```text
[redacted sensitive answer]
```

- Access the database and discover the encrypted credentials. What is the name of the database you find these in?
```text
[redacted sensitive answer]
```

- Crack the password. What is it?
```text
[redacted sensitive answer]
```

- Use su to login to the newly discovered user by exploiting password reuse.
```text
[redacted sensitive answer]
```

- What is the value of the user.txt flag?
```text
[redacted challenge flag]
```

- Check the user's groups. Which group can be leveraged to escalate privileges?
```text
lxd
```

- Abuse this group to escalate privileges to root.
```text
refer Hacking Article lxd privileage escalation
```

- What is the value of the root.txt flag?
```text
[redacted challenge flag]
```
