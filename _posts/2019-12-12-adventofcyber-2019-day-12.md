---
title: "TryHackMe Advent of Cyber 2019 Day 12"
date: 2019-12-12
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2019"
event_day: "Day 12"
permalink: "/writeups/advent-of-cyber/adventofcyber-2019-day-12/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2019
  - day-12
---

# Elfcryption

```text
gpg is used to encrypt file
Symmetric encryption [ie, same key to encrypt and decrypt]
gpg -e filename  --> encrypt with a password
gpg -d filename.gpg ---> decrypt using same password

md5sum data.txt --> it will give you a hash value of that file.
Try updating the files content and running the command again on the file, it will be different.
''''
```
Let’s generate some public/private keys and encrypt/decrypt a message!

To generate a private key we use the following command (8912 creates the key 8912 bits long):
    openssl genrsa -aes256 -out private.key 8912

To generate a public key we use our previously generated private key:
    openssl rsa -in private.key -pubout -out public.key

Lets now encrypt a file (plaintext.txt) using our public key:
    openssl rsautl -encrypt -pubin -inkey public.key -in plaintext.txt -out encrypted.txt

Now, if we use our private key, we can decrypt the file and get the original message:
    openssl rsautl -decrypt -inkey private.key -in encrypted.txt -out plaintext.txt

''''''

## Task
- What is the md5 hashsum of the encrypted note1 file?
```text
24cf615e2a4f42718f2ff36b35614f8f
```

- Where was elf Bob told to meet Alice?
```text
Santa's Grotto      --via gpg -d note1.txt.gpg  [password: redacted]]
```

- Decrypt note2 and obtain the flag!
```text
[redacted challenge flag]
```
