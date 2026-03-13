---
title: "TryHackMe Advent of Cyber 2019 Day 1"
date: 2019-12-01
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2019"
event_day: "Day 1"
permalink: "/writeups/advent-of-cyber/adventofcyber-2019-day-1/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2019
  - day-1
---

# christmas-one

```text
First register account in that website
the login with that username:pass and catch the login by brupsuit and intercept it
we can see that it users cookie ---[redacted] < answer 1 >

encode cookie value
they use same cookie for everytime login it is not changing so we can exploit that
log out and create another account with different username and intercepted
encode cookie value has a fixed  part < answer 2 >

make another decoded cookie value with name [mcinventory + the fixed part]
and catch the request and intercept the response
change the cookie value
login mcinventory account < answer 3 >
```

## Task

- What is the name of the cookie used for authentication?
```text
authid
```

- If you decode the cookie, what is the value of the fixed part of the cookie?
```text
v4er9ll1!ss
```

- After accessing his account, what did the user mcinventory request?
```text
firewall
```
