---
layout: page
title: "/easypeasy"
permalink: "/writeups/tryhackme/easypeasy/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Easy Peasy"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect easypeasy</p>
  <h1>Easy Peasy</h1>
  <p>Linux room covering service enumeration, initial access, and privilege escalation. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">5 docx note</span>
    <span class="tag">5 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Easy Peasy is usually approached as a staged Linux/web challenge: enumerate multiple HTTP surfaces, recover clues and hashes from hidden content, crack the supplied materials, pivot to SSH, and complete privilege escalation through a writable scheduled-task or weak automation path.</p>
  <div class="tag-list">
    <span class="tag">multi-port web enumeration</span>
    <span class="tag">hash cracking</span>
    <span class="tag">hidden content discovery</span>
    <span class="tag">SSH pivot</span>
    <span class="tag">cron or automation abuse</span>
  </div>
</section>

## Notes

## Recon

- Service enumeration identifies multiple web surfaces and a non-standard SSH port, which signals a layered challenge rather than a single vulnerable app.
- Directory and content discovery are central to the room. Hidden paths and embedded clues reveal the flags, password material, and the route to the foothold.

## Initial Access

- The intended route is to recover and crack the exposed hash material using the wordlist context provided by the room artifacts.
- Once the credentials are recovered, they are reused against SSH to establish the user shell on the Linux host.

## Privilege Escalation

- Post-exploitation focuses on weak automation or writable scheduled-task behavior.
- The path to root is not about a kernel exploit; it is about careful local enumeration and abuse of the host’s automation workflow.

## Security Notes

- Multi-port web exposure increases the chance that a hidden or less-monitored application becomes the real point of compromise.
- Recoverable hashes are effectively credentials once an attacker has enough context to crack them.
- Cron jobs and writable automation paths remain one of the most common avoidable Linux privilege-escalation problems.

## Supporting Files

### Easypeasy

123456
12345
123456789
password
iloveyou
princess
1234567
rockyou
louise
orange
789456
999999
shorty
11111
12345678
abc123
nicole
daniel
babygirl
monkey
lovely
jessica
654321
michael
ashley
qwerty
111111
iloveu
000000
michelle
tigger
sunshine
12345678
abc123
nicole
daniel
babygirl
monkey
lovely
jessica
654321
michael
ashley
qwerty
111111
iloveu
000000
michelle
123456
12345
123456789
password
iloveyou
princess
1234567
rockyou
12345678
abc123
nicole
123456
12345
123456789
password
iloveyou
princess
1234567
rockyou
12345678
abc123
nicole
daniel
babygirl
monkey
lovely
jessica
654321
michael
ashley
qwerty
111111
iloveu
daniel
babygirl
monkey
lovely
jessica
654321
michael
ashley
qwerty
111111
iloveu
tigger
sunshine
chocolate
password1
soccer
anthony
paintball
love4u
lilone
kaycee
ethan1
beauty1
angelgirl
alegria
vladimir
tulips
pebbles1
mason
sweetiepie
summer07
snoopdogg
snickers1
raphael
panama
mummy
maryrose
jumong
111111
iloveu
000000
michelle
tigger
sunshine
chocolate
password1
soccer
anthony
fresa
energy
bacardi
yumyum
underground
shane1
olivia1
paintball
imcute
fresa
energy
bacardi
yumyum
underground
shane1
olivia1
navarro
brodie
bribri
anabel
12qwaszx
sexy11
pppppp
party
mario1
juicy
corazones
smarty
selina
ANDREA
7895123
654123
19871987
waters
vampires
password1
soccer
anthony
friends
butterfly
ANDREA
7895123
654123
19871987
waters
vampires
password1
soccer
anthony
friends
butterfly
mookie
fresita
leelee
tequieromucho
harry
giovanni
ranger
celticfc
tagged
snuggles
preston
newcastle
austin1
sniper
erica
stefan
ecuador
hotpink
soulmate
shutup
1qaz2wsx
taytay
sassy
iverson3
playboy1
lunita
honey1
951753
thomas1
bernard
peace
arthur
12345a
marlboro
merlin
southside
loser1
brandi
arlene
blueeyes
michel
rachelle
mackenzie
ernesto
champion
missy
mamapapa
fatboy
darius
282828
edgar
alexia
landon
nicola
99999
nancy
hermione
cosita
nissan
michele
starlight
unique
tiger1
rivera
morales
coolcat
steelers
judith
dimples
chocolate1
viviana
rodney
iluvu
maurice
katelyn
carrie
111222
gonzalez
softball1
random
kennedy
esperanza
pierre
moonlight
baby12
spirit
love22
nintendo
marlene
234567
shasha
snowflake
children
stanley
newlife
goober
doraemon
ingrid
father
77777
geraldine
dimple
dillon
romance
bunny
bhaby
winner
tweetybird
kathryn
paramore
allstar
abcde
something
runescape
jermaine
jefferson
pitbull
seventeen
romania
france
emotional
nigger
mariela
fucku
bitchy
ballin
loveless
smallville
ricky
peluche
godbless
blue123
alonso
meghan
garrett
mykids
mexico1
clover
vanesa

### Robots

ObsJmP173N2X6dOrAgEAL0Vu

### Secrettext

username:boring
password: [redacted sensitive value] sensitive value] 01100011 01101111 01101110 01110110 01100101 01110010 01110100 01100101 01100100 01101101 01111001 01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 01110100 01101111 01100010 01101001 01101110 01100001 01110010 01111001

## Collected Output

### gobuster-apache

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.138.0:65524
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/06/27 17:44:28 Starting gobuster in directory enumeration mode
===============================================================

/server-status        (Status: 403) [Size: 279]
===============================================================
2021/06/27 18:13:15 Finished
===============================================================
```

### gobuster-dir

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.138.0
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/06/27 15:56:39 Starting gobuster in directory enumeration mode
===============================================================

/hidden               (Status: 301) [Size: 169] [--> http://10.10.138.0/hidden/]
===============================================================
2021/06/27 16:28:51 Finished
===============================================================
```

### gobuster-dir-hidden

```text
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.138.0/hidden/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/06/27 16:20:24 Starting gobuster in directory enumeration mode
===============================================================

/whatever             (Status: 301) [Size: 169] [--> http://10.10.138.0/hidden/whatever/]
```

### nmap-full_port

```text
# Nmap 7.91 scan initiated Sun Jun 27 16:43:41 2021 as: nmap -p- -oN nmap-full_port -vv 10.10.138.0
```

### nmap-initial

```text
# Nmap 7.91 scan initiated Sun Jun 27 15:55:12 2021 as: nmap -sV -sC -A -oN nmap-initial -v 10.10.138.0
Nmap scan report for 10.10.138.0
Host is up (0.51s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.16.1
| http-methods: 
|_  Supported Methods: GET HEAD
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: nginx/1.16.1
|_http-title: Welcome to nginx!
Aggressive OS guesses: Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 2.6.32 (92%), Linux 3.1 - 3.2 (92%), Linux 3.11 (92%), Linux 3.2 - 4.9 (92%), Linux 3.7 - 3.10 (92%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 48.888 days (since Sun May  9 18:36:57 2021)
Network Distance: 4 hops
TCP Sequence Prediction: Difficulty=263 (Good luck!)
IP ID Sequence Generation: All zeros

TRACEROUTE (using port 256/tcp)
HOP RTT       ADDRESS
1   587.79 ms 10.2.0.1
2   ... 3
4   589.47 ms 10.10.138.0

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jun 27 15:56:18 2021 -- 1 IP address (1 host up) scanned in 66.77 seconds
```
