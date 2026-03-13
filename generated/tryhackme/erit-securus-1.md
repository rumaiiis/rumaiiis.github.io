---
layout: writeup
title: "/erit-securus-1"
permalink: "/writeups/tryhackme/erit-securus-1/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Erit Securus 1"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect erit-securus-1</p>
  <h1>Erit Securus 1</h1>
  <p>General mixed challenge room blending enumeration, exploitation, and post-exploitation practice. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Challenge Labs</strong>.</p>
  <div class="tag-list">
    <span class="tag">Challenge Labs</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">3 docx note</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Workflow Focus</h2>
  <p>General mixed challenge room blending enumeration, exploitation, and post-exploitation practice. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Operator Notes

## Recon

- This room mixes discovery, analysis, and exploitation, so the right path usually appears only after multiple clues are combined.
- Erit Securus 1 rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- Initial access depends on linking those clues together rather than relying on a single obvious vulnerability.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- After the foothold, the room transitions into standard host enumeration and local privilege-escalation review.
- After the foothold, local context matters more than noisy exploitation.

## Defensive Takeaway

- The defensive lesson is that seemingly minor leaks across different services often combine into full compromise when an attacker is systematic.

## Supporting Notes

### Requirements

requests
sys
warnings
re
os
bs4
colorama
colored

### Session

2812219f3a185535273be85f6701944f
447b386f8f948f7ab2cce2ffba6fb644
62da1cae39d8567d18db22929a57e544
2812219f3a185535273be85f6701944f
447b386f8f948f7ab2cce2ffba6fb644
62da1cae39d8567d18db22929a57e544
6efac4fc81478c681f48070993b13305
c92c3d02b465c24c95b1300aba3199b3
01c87e7e4b4b4a70a6e62c29a58452cd
101580d4735e240b70756256dcd4304c
1eb38d2eceaff901276bf2ccfb25c391
27e316fae78425166be77df2cba459a6
2d32c1c8dfb08b9adb623aa69c0efaef
33870a71312eb125d5e42c552edc15fa
47bd21a84b8a3c36cd3026492d1ebc91
49ea27acc7984555fd9697d676fc65db
4f6c3f01b5e2b98b8ef40a8216b2e9fc
68e03dc0219fb2c00f1bc8f0eda332c3
a206b90d43da1fc1c8fae914b8b2d5c8
01c87e7e4b4b4a70a6e62c29a58452cd
101580d4735e240b70756256dcd4304c
1eb38d2eceaff901276bf2ccfb25c391
27e316fae78425166be77df2cba459a6
2d32c1c8dfb08b9adb623aa69c0efaef
33870a71312eb125d5e42c552edc15fa
47bd21a84b8a3c36cd3026492d1ebc91
49ea27acc7984555fd9697d676fc65db
4f6c3f01b5e2b98b8ef40a8216b2e9fc
68e03dc0219fb2c00f1bc8f0eda332c3
83f0a127f1f3b3b7c75b9e04e77ad58e
a206b90d43da1fc1c8fae914b8b2d5c8
a29ab330254a9fcc71b871c48b8a8ad8
bd3d3f7d888a19b5e0c4bf2bb24d2619
cf6979e607dcb4ca5102848734e77cb1
ddec07b44150c5bef972069d4faa85a8
e5fe3e841937d83e177b2d9597bbc472
f104824edcb8459db78dc0279751dee0

## Evidence Pack

### nmap-initial

```text
# Nmap 7.91 scan initiated Wed Jun 23 10:00:21 2021 as: nmap -sV -sC -A -oN nmap-initial 10.10.242.51
Nmap scan report for 10.10.242.51
Host is up (0.49s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 6.7p1 Debian 5+deb8u8 (protocol 2.0)
| ssh-hostkey: 
|   1024 b1:ac:a9:92:d3:2a:69:91:68:b4:6a:ac:45:43:fb:ed (DSA)
|   2048 3a:3f:9f:59:29:c8:20:d7:3a:c5:04:aa:82:36:68:3f (RSA)
|   256 f9:2f:bb:e3:ab:95:ee:9e:78:7c:91:18:7d:95:84:ab (ECDSA)
|_  256 49:0e:6f:cb:ec:6c:a5:97:67:cc:3c:31:ad:94:a4:54 (ED25519)
80/tcp open  http    nginx 1.6.2
|_http-generator: Bolt
|_http-server-header: nginx/1.6.2
|_http-title: Graece donan, Latine voluptatem vocant. | Erit Securus 1
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.91%E=4%D=6/23%OT=22%CT=1%CU=44641%PV=Y%DS=4%DC=T%G=Y%TM=60D2B92
OS:C%P=x86_64-pc-linux-gnu)SEQ(SP=101%GCD=1%ISR=10A%TI=Z%CI=I%II=I%TS=8)SEQ
OS:(SP=100%GCD=1%ISR=108%TI=Z%II=I%TS=8)OPS(O1=M505ST11NW7%O2=M505ST11NW7%O
OS:3=M505NNT11NW7%O4=M505ST11NW7%O5=M505ST11NW7%O6=M505ST11)WIN(W1=68DF%W2=
OS:68DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)ECN(R=Y%DF=Y%T=40%W=6903%O=M505NNSN
OS:W7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%D
OS:F=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O
OS:=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W
OS:=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%R
OS:IPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 256/tcp)
HOP RTT       ADDRESS
1   514.37 ms 10.2.0.1
2   ... 3
4   630.93 ms 10.10.242.51

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jun 23 10:01:40 2021 -- 1 IP address (1 host up) scanned in 81.32 seconds
```
