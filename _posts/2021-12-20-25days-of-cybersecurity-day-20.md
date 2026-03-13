---
title: "TryHackMe Advent of Cyber 2020 Day 20"
date: 2021-12-20
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2020"
event_day: "Day 20"
permalink: "/writeups/advent-of-cyber/25days-of-cybersecurity-day-20/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2020
  - day-20
---

# PowershELF to the rescue

```text
PowerShell is a cross-platform task automation and configuration management framework, consisting of a command-line shell and scripting language.
 Unlike most shells, which accept and return text, PowerShell is built on top of the .NET Common Language Runtime (CLR), and accepts and returns .NET objects. This fundamental change brings entirely new tools and methods for automation.
```

```text
PowerShell commands are known as cmdlets.

To list the content of current directory we use : Get-Chiditem
there are various other options to:
	-Path : to specify path or one or more location, even wildcard to

	-File / -Directory : to get list of file or directory

	-Filter : specifies a filter to qualify the Path parameter.

	-Recurse : Gets the item in the specific locations and in all child items of the locations.

	-Hidden : to get only hidden item

	-ErrorAction SilentlyContinue : Specifies what action to take if the command encounters an error.

eg: Get-childitem -Hidden -File -ErrorAction SilentlyContinue
	to view hidden files in current directories
```

```text
Another cmdlets is : Get-Content
this allow to read content of a file

eg: Get-Content -Path file.txt

TO findout number of words in a file we can use Get-Content and pipe the result to Measure Object cmdlet.

eg: Get-Content -Path file.txt | Measure-Object -Word
```

```text
To get the exact position of a string within the file, you can use the following command:  (Get-Content -Path file.txt)[index]
```

```text
To change diectories use : Set-Location

eg: Set-Location -Path c:\users\administratoe\desktop
```

```text
to search a perticular file of pattern : Select-String

eg: Select-String -Path 'c:\users\administrstor\desktop' -Pattern "*.pdf*"
```

```text
we can always use Get-Help to view about the cmdlet.

eg: Get-Help Select-String
```

## Task

- Search for the first hidden file elf file within Document folder. Read the content of the file. What does Elf 1 want?
```text
2 front teeth          -via Get-Childitem -Path .\Documents\ -Hidden -File
```

- Search on the desktop for a hidden folder that contains the file for Elf 2. Read the contents of this file. What is the name of that movie that Elf 2 wants?
```text
Scrooged		-via Get-Childrenitem -Path .\Desktop\ -Hidden -Directory
```

- Search the Windows directory for a hidden folder that contains files for Elf 3. What is the name of the hidden folder? (This command will take a while)
```text
3lfthr3e			-via Get-ChildItem -Path C:\Windows\System32\ -Hidden -Directory -Filter "*3*"
```

- How many words does the first file contain?
```text
9999			-via  Get-Content -Path C:\Windows\System32\3lfthr3e\1.txt | measure-object -Word
```

- What 2 words are at index 551 and 6991 in the first file?
```text
Red Ryder               -via (Get-Content .\1.txt)[551] and (Get-Content .\1.txt)[6991]
```

- This is only half the answer. Search in the 2nd file for the phrase from the previous question to get the full answer. What does Elf 3 want? (use spaces when submitting the answer)
```text
red ryder bb gun  	-via  Select-String -Path .\2.txt -pattern redryder
```
