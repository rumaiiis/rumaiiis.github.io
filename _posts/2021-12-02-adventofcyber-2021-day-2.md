---
title: "TryHackMe Advent of Cyber 2021 Day 2"
date: 2021-12-02
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2021"
event_day: "Day 2"
permalink: "/writeups/advent-of-cyber/adventofcyber-2021-day-2/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2021
  - day-2
---

# Day 2

		Elf HR Problems
computer and webserver to commmunicate with each other an intermediary protocol os requires. this is where the http (hyper test transfer protocol) is introduced.

When an http request is crafted, the method and target header will always be included.
	target - specify what ton retrive from the server
	method - specify how. (GET POST)

Cookies:
	these are small piece of data(metadata) or information locally stored on our computer that are sent to the server whrn you make a request.
	cookies can be assigned any name and any value allowing the webserver to store any information it wants.

Authentication cookies or session cookies:
	these are used to identify you and what access level is attacjed to ypur sesesion.

Task

- no answer

- What is the name of the new cookie that was created for your account?
```text
user-auth
```

- What encoding type was used for the cookie value?
```text
hexadecimal
```

- What object format is the data of the cookie stored in?
```text
JSON
''

5. What is the value of the administrator cookie? (username = admin)
```
7b636f6d70616e793a2022546865204265737420466573746976616c20436f6d70616e79222c206973726567697374657265643a2254727565222c20757365726e616d653a2261646d696e227d
```text
6. What team environment is not responding?
```
HR
```text
7. What team environment has a network warning?
```
Application
```text
==========================================
```
