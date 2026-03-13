---
layout: writeup
title: "/vulnnet-internal"
permalink: "/writeups/tryhackme/vulnnet-internal/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "VulnNet Internal"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect vulnnet-internal</p>
  <h1>VulnNet Internal</h1>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Primary writeup exists in local notes. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">1 markdown source</span>
    <span class="tag">3 docx note</span>
    <span class="tag">1 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Attack Path Overview</h2>
  <p>Public walkthroughs and the official room description both point to this box being centered on internal-service enumeration. The common methodology is to enumerate SMB/NFS-style internal services, recover business files or service data, use those artifacts to discover additional internal access paths, and pivot from exposed internal resources to a local user shell before final privilege escalation.</p>
  <div class="tag-list">
    <span class="tag">internal service enumeration</span>
    <span class="tag">SMB/NFS data exposure</span>
    <span class="tag">artifact-driven enumeration</span>
    <span class="tag">pivoting to local access</span>
    <span class="tag">Linux privilege escalation</span>
  </div>
</section>

## Operator Notes

## Recon

- The room is built around internal-service exposure rather than a public web exploit, so NFS, SMB, and related services become the primary focus immediately.
- Business files and service-side artifacts provide the clues that link one exposed service to the next access path.

## Initial Access

- The intended route is to enumerate the accessible internal services, recover sensitive files or notes, and use those to pivot toward a user foothold.
- Artifact-driven enumeration matters more here than exploit noise; the environment leaks the path if each service is examined properly.

## Privilege Escalation

- Once local access is established, the final step depends on standard Linux host enumeration and trust abuse.
- The box is designed to reward systematic movement from service exposure to host-level privilege.

## Defensive Takeaway

- Internal file services are often treated as low-risk, but they frequently expose the exact documents and credentials an attacker needs to pivot.
- Business data, not just config files, can become the key intelligence source during an intrusion.
- Segmentation and least-privilege access to internal shares are as important as patching edge services.

## Supporting Notes

### Business Req

We just wanted to remind you that we’re waiting for the DOCUMENT you agreed to send us so we can complete the TRANSACTION we discussed.
If you have any questions, please text or phone us.

### Data

Purge regularly data that is not needed anymore

### Services

[redacted challenge flag]

## Evidence Pack

### nmap-initial

```text
# Nmap 7.91 scan initiated Thu Jul  8 17:35:00 2021 as: nmap -sC -sV -oN nmap-initial 10.10.112.231
Nmap scan report for 10.10.112.231
Host is up (0.71s latency).
Not shown: 808 closed ports, 186 filtered ports
PORT     STATE SERVICE    VERSION
22/tcp   open  tcpwrapped
| ssh-hostkey: 
|   2048 5e:27:8f:48:ae:2f:f8:89:bb:89:13:e3:9a:fd:63:40 (RSA)
|   256 f4:fe:0b:e2:5c:88:b5:63:13:85:50:dd:d5:86:ab:bd (ECDSA)
|_  256 82:ea:48:85:f0:2a:23:7e:0e:a9:d9:14:0a:60:2f:ad (ED25519)
111/tcp  open  tcpwrapped
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      39305/udp   mountd
|   100005  1,2,3      42799/tcp6  mountd
|   100005  1,2,3      48755/udp6  mountd
|   100005  1,2,3      48799/tcp   mountd
|   100021  1,3,4      38705/tcp   nlockmgr
|   100021  1,3,4      42459/tcp6  nlockmgr
|   100021  1,3,4      44485/udp   nlockmgr
|   100021  1,3,4      46375/udp6  nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
139/tcp  open  tcpwrapped
445/tcp  open  tcpwrapped Samba smbd 4.7.6-Ubuntu
873/tcp  open  tcpwrapped
2049/tcp open  tcpwrapped

Host script results:
|_clock-skew: mean: -39m58s, deviation: 1h09m15s, median: 0s
|_nbstat: NetBIOS name: VULNNET-INTERNA, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: vulnnet-internal
|   NetBIOS computer name: VULNNET-INTERNAL\x00
|   Domain name: \x00
|   FQDN: vulnnet-internal
|_  System time: 2021-07-08T14:05:20+02:00
| smb-security-mode: 
|   account_used: guest
|
```
