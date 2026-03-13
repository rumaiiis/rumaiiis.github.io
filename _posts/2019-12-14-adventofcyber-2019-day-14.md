---
title: "TryHackMe Advent of Cyber 2019 Day 14"
date: 2019-12-14
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2019"
event_day: "Day 14"
permalink: "/writeups/advent-of-cyber/adventofcyber-2019-day-14/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2019
  - day-14
---

# Unknown Storage

```text
In the past, the default S3 permissions were weak and S3 buckets would be publicly accessible but AWS changed this to block public access by default.
```

```text
Once we have an s3 bucket, we can check if it’s publicly accessible by browsing to the URL. The format of the URL is:
bucketname.s3.amazonaws.com
```

```text
McSkidy's only starting point is a single bucket name: advent-bucket-one
advent-bucket-one.s3.amazonaws.com
```

## Task

- What is the name of the file you found?
```text
employee_names.txt           --via http://advent-bucket-one.s3.amazonaws.com
```

- What is in the file?
```text
mcchef                     --via http://advent-bucket-one.s3.amazonaws.com/employee_names.txt
```
