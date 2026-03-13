---
title: "TryHackMe Advent of Cyber 2020 Day 6"
date: 2021-12-06
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2020"
event_day: "Day 6"
permalink: "/writeups/advent-of-cyber/25days-of-cybersecurity-day-6/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2020
  - day-6
---

# Aoc Day6

```text
Cross-site Scripting (XXS) is a web vulnerability that allows an attacker to  the interactions that user have a vulnerable application.
XXS allow an attacker to masquarite as a victim user. If the victim user has privilege access within application (ie.admin), then the attack might be able to gain full control.
''''
```
Types of XSS
-> Stored XSS
	Stored XSS works when a certain malicious JavaScript is submitted and later on stored directly on the website.

--> Reflected XSS
	Refected XSS that is carried out directly in the HTTP request and requires the attacker to do a bit more work.

```text
# TASK

1. No answer

2. What vulnerability type was used to eploit the application?
```
Stored Cross-site Scripting
```text
3. What query string can be abused to craft a reflected XSS?
```
q
```text
4. No answer

5. Run a ZAP automated scan on the target. How many XSS alert are in the scan?
```
2
```text
6. No answer

============================================================================
```
