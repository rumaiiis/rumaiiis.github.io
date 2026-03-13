---
title: "TryHackMe Advent of Cyber 2020 Day 17"
date: 2021-12-17
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2020"
event_day: "Day 17"
permalink: "/writeups/advent-of-cyber/25days-of-cybersecurity-day-17/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2020
  - day-17
---

# aoccmnre1

```text
Machine code is usually represented by more readable form of the code called assembly code.

before an executable file is produced, the source code is first compiled into assembly code(.s file),
 after which the assembly converts it into an object program(.o file),
 and operations with the linker finally make it an executable.

radare2 is a framework for reverse engineering and analysing binaries.
it can be used to dissamble binaries(transialte machine code to assembly)
''''
```
ip: 10.10.3.179

ssh
Username: elfmceager
Password: [redacted]
```text
[redacted sensitive answer]
```
After login we see two executable file - file1, challenge1

To see what happens behind run: r2 -d ./file1
this will open the binary in debugging mode.
fist thing to do is ask r2 to analyze the program by : aa

For general help, we can run: ? or if we wish to understand more about a specific feature, we could provide a?

most programs have an entry point defined as main. To find the list of the funtions run: afl
afl | grep main

lets examine the assembly code at main by running the command "pdf @main", where pdf means print deassembly function

Some other important instructions are:
    leaq source, destination: this instruction sets destination to the address denoted by the expression in source
    addq source, destination: destination = destination + source
    subq source, destination: destination = destination - source
    imulq source, destination: destination = destination * source
    salq source, destination: destination = destination << source where << is the left bit shifting operator
    sarq source, destination: destination = destination >> source where >> is the right bit shifting operator
    xorq source, destination: destination = destination XOR source
    andq source, destination: destination = destination & source
    orq source, destination: destination = destination | source

setting break point : db 0x00400b55
Running dc will execute the program until we hit the breakpoint
Once we hit the breakpoint and print out the main function, the rip which is the current instruction shows where execution has stopped

To view the contents of the local_ch variable, we use the following instruction px @memory-address In this case,
 the corresponding memory address for local_ch will be rbp-0xc ( from the first few lines of @pdf main)
 This instruction prints the values of memory in hex:

```text
# TASK

r2 -d ./challenge1

1.  What is the value of local_ch when its corresponding movl instruction is called (first if multiple)?
```
1
```text
2. What is the value of eax when the imull instruction is called?
```
6
```text
3. What is the value of local_4h before eax is set to 0?
```
6
```text
================================================================
```
