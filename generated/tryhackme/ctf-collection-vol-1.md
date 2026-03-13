---
layout: page
title: "/ctf-collection-vol-1"
permalink: "/writeups/tryhackme/ctf-collection-vol-1/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "CTF Collection Vol.1"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect ctf-collection-vol-1</p>
  <h1>CTF Collection Vol.1</h1>
  <p>Mixed challenge room covering enumeration, exploitation, and post-exploitation practice. This page combines the local notes, supporting artifacts, and a cleaned-up summary of the room path.</p>
</section>

<section class="panel">
  <h2>Room Details</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Challenge Labs</strong>.</p>
  <div class="tag-list">
    <span class="tag">Challenge Labs</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">2 docx note</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Summary</h2>
  <p>Mixed challenge room covering enumeration, exploitation, and post-exploitation practice. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Notes

## Recon

- This room mixes discovery, analysis, and exploitation, so the right path usually appears only after multiple clues are combined.
- CTF Collection Vol.1 rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- Initial access depends on linking those clues together rather than relying on a single obvious vulnerability.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- After the foothold, the room transitions into standard host enumeration and local privilege-escalation review.
- After the foothold, local context matters more than noisy exploitation.

## Security Notes

- The defensive lesson is that seemingly minor leaks across different services often combine into full compromise when an attacker is systematic.

## Supporting Files

### Final Message

It going to be over soon. Sleep my child.
[redacted challenge flag]

### Hello There

Thank you for extracting me, you are the best!
[redacted challenge flag]

## Collected Output

### spoil_hex_data

```text
89504E470D0A1A0A0000000d4948445200000320000003200806000000db
700668000000017352474200aece1ce9000000097048597300000ec40000
0ec401952b0e1b0000200049444154789cecdd799c9c559deff1cf799e5a
bb7a5f927477f640480209201150c420bba288a8805c19067c5d64c079e9
752e03ce38e30e8e2f75e63a23ea8c0ce8308e036470c191cd80880c4b20
0909184c42b64ed2e9f4bed7f23ce7fe51559dea4e27a4bbaaf7effbf5ea
57d2d5554f9daa7abafa7ceb9cf33bc65a6b1111111111111907ce443740
4444444444660e0510111111111119370a202222222222326e1440444444
444464dc28808888888888c8b8510011111111119171a300222222222222
e34601444444444444c68d028888888888888c1b0510111111111119370a
202222222222326e1440444444444464dc28808888888888c8b851001111
1111119171a300222222222222e34601444444444444c68d028888888888
888c1b0510111111111119370a202222222222326e1440444444444464dc
28808888888888c8b8510011111111119171a300222222222222e3460144
4444444444c68d028888888888888c1b0510111111111119370a20222222
2222326e1440444444444464dc28808888888888c8b85100111111111191
71a300222222222222e34601444444444444c68d028888888888888c1b05
10111111111119370a202222222222326e1440444444444464dc28808888
888888c8b8510011111111119171a300222222222222e346014444444444
44c68d028888888888888c1b0510111111111119370a202222222222326e
1440444444444464dc28808888888888c8b8510011111111119171a30022
2222222222e34601444444444444c68d028888888888888c1b0510111111
111119370a202222222222326e1440444444444464dc28808888888888c8
b8510011111111119171a300222222222222e32630d10d10996aacef83b5
18d71d74b9dfdb8bd7db4baabd1dafbb9b545717a9ae2e6c3c8e4da5f0ba
bac018bcfe7efcfe7e0c60ad3de2f8c618acb504caca308e038e83535484
1b89e0c462389108c192129c9212829595044a4ac098c107f1fdf465432f
171111119960c60ed7031291c3acc5fa7e3a0c643bf4d6926c69a17bcb16
e27bf6d0bf6b177d3b77926c6b23be7f3fb6ab8b683c0e9e87053cdfc74b
a5b0a44387e7fb99c31c3d8084028181fb0b040238c610741ce28e433c1a
2558594978de3c42b36611aeada568c50aa24b9610993f1f37163bdcfc54
0a1c27dd7e1111119109a60022720cd6f7c1f7b1c9247e3c4ed7a64d74fc
ee77f46cde4cff9e3d240e1ec4767612b5160ff08014e01b
```
