---
layout: writeup
title: "/kenobi"
permalink: "/writeups/tryhackme/kenobi/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Kenobi"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect kenobi</p>
  <h1>Kenobi</h1>
  <p>Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Linux and PrivEsc</strong>.</p>
  <div class="tag-list">
    <span class="tag">Linux and PrivEsc</span>
    <span class="tag">2 docx note</span>
    <span class="tag">2 command artifact</span>
  </div>
</section>

<section class="panel">
  <h2>Attack Path Overview</h2>
  <p>The standard Kenobi path is to enumerate SMB and NFS exposure, recover SSH key clues from the anonymous share, abuse the vulnerable ProFTPD copy commands to move the private key into a mountable location, log in over SSH, and finish with PATH hijacking against a SUID binary.</p>
  <div class="tag-list">
    <span class="tag">SMB share discovery</span>
    <span class="tag">NFS enumeration</span>
    <span class="tag">ProFTPD mod_copy abuse</span>
    <span class="tag">SSH key recovery</span>
    <span class="tag">PATH hijack via SUID</span>
  </div>
</section>

## Operator Notes

## Recon

- Network enumeration shows a Linux target exposing `ftp`, `ssh`, `http`, `rpcbind`, `smb`, and `nfs`.
- SMB enumeration is the first productive branch. The anonymous share contains operational data, including the `log.txt` clue that references key generation activity.
- RPC/NFS enumeration reveals a mountable path that becomes useful later in the attack chain.

## Initial Access

- Service fingerprinting on FTP points to a ProFTPD build affected by the `mod_copy` abuse path.
- The practical workflow is to use `SITE CPFR` and `SITE CPTO` to copy Kenobi's private key into a location reachable through the exposed NFS mount.
- After mounting the exported path, the recovered SSH key can be used to authenticate as the user and establish the foothold.

## Privilege Escalation

- Local enumeration of SUID binaries identifies `/usr/bin/menu` as the interesting target.
- String inspection shows commands being called without absolute paths, which makes `PATH` hijacking the intended escalation route.
- By placing a controlled binary earlier in `PATH`, the SUID program can be coerced into spawning a root shell.

## Defensive Takeaway

- Anonymous SMB shares often leak more operational context than expected.
- Exposed NFS paths and legacy FTP services are dangerous when combined with a write or copy primitive.
- SUID programs that call external binaries without full paths are a recurring Linux privilege-escalation flaw.

## Supporting Notes

### Log

Generating public/private rsa key pair.
Enter file in which to save the key (/home/kenobi/.ssh/id_rsa):
Created directory '/home/kenobi/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/kenobi/.ssh/id_rsa.
Your public key has been saved in /home/kenobi/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:C17GWSl/v7KlUZrOwWxSyk+F7gYhVzsbfqkCIkr2d7Q kenobi@kenobi
The key's randomart image is:
+---[RSA 2048]---[redacted]
|                 |
|           ..    |
|        . o. .   |
|       ..=o +.   |
|      . So.o++o. |
|  o ...+oo.Bo*o  |
| o o ..o.o+.@oo  |
|  . . . E .O+= . |
|     . .   oBo.  |
+---[redacted][SHA256]---[redacted]
# This is a basic ProFTPD configuration file (rename it to
# 'proftpd.conf' for actual use.  It establishes a single server
# and a single anonymous login.  It assumes that you have a user/group
# "nobody" and "ftp" for normal operation and anon.
ServerName"ProFTPD Default Installation"
ServerTypestandalone
DefaultServeron
# Port 21 is the standard FTP port.
Port21
# Don't use IPv6 support by default.
UseIPv6off
# Umask 022 is a good standard umask to prevent new dirs and files
# from being group and world writable.
Umask022
# To prevent DoS attacks, set the maximum number of child processes
# to 30.  If you need to allow more than 30 concurrent connections
# at once, simply increase this value.  Note that this ONLY works
# in standalone mode, in inetd mode you should use an inetd server
# that allows you to limit maximum number of processes per service
# (such as xinetd).
MaxInstances30
# Set the user and group under which the server will run.
Userkenobi
Groupkenobi
# To cause every FTP user to be "jailed" (chrooted) into their home
# directory, uncomment this line.
#DefaultRoot ~
# Normally, we want files to be overwriteable.
AllowOverwriteon
# Bar use of SITE CHMOD by default
<Limit SITE_CHMOD>
DenyAll
</Limit>
# A basic anonymous configuration, no upload directories.  If you do not
# want anonymous users, simply delete this entire <Anonymous> section.
<Anonymous ~ftp>
Userftp
Groupftp
# We want clients to be able to login with "anonymous" as well as "ftp"
UserAliasanonymous ftp
# Limit the maximum number of anonymous logins
MaxClients10
# We want 'welcome.msg' displayed at login, and '.message' displayed
# in each newly chdired directory.
DisplayLoginwelcome.msg
DisplayChdir.message
# Limit WRITE everywhere in the anonymous chroot
<Limit WRITE>
DenyAll
</Limit>
</Anonymous>
#
# Samp

## Evidence Pack

### nmap-initial

```text
# Nmap 7.91 scan initiated Thu Jun 17 17:15:51 2021 as: nmap -sS -sV -sC -vv -oN ./nmap-initial 10.10.213.207
Nmap scan report for 10.10.213.207
Host is up, received echo-reply ttl 61 (0.66s latency).
Scanned at 2021-06-17 17:15:56 IST for 49s
Not shown: 993 closed ports
Reason: 993 resets
PORT     STATE SERVICE     REASON         VERSION
21/tcp   open  ftp         syn-ack ttl 61 ProFTPD 1.3.5
22/tcp   open  ssh         syn-ack ttl 61 OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b3:ad:83:41:49:e9:5d:16:8d:3b:0f:05:7b:e2:c0:ae (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8m00IxH/X5gfu6Cryqi5Ti2TKUSpqgmhreJsfLL8uBJrGAKQApxZ0lq2rKplqVMs+xwlGTuHNZBVeURqvOe9MmkMUOh4ZIXZJ9KNaBoJb27fXIvsS6sgPxSUuaeoWxutGwHHCDUbtqHuMAoSE2Nwl8G+VPc2DbbtSXcpu5c14HUzktDmsnfJo/5TFiRuYR0uqH8oDl6Zy3JSnbYe/QY+AfTpr1q7BDV85b6xP97/1WUTCw54CKUTV25Yc5h615EwQOMPwox94+48JVmgE00T4ARC3l6YWibqY6a5E8BU+fksse35fFCwJhJEk6xplDkeauKklmVqeMysMWdiAQtDj
|   256 f8:27:7d:64:29:97:e6:f8:65:54:65:22:f7:c8:1d:8a (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBpJvoJrIaQeGsbHE9vuz4iUyrUahyfHhN7wq9z3uce9F+Cdeme1O+vIfBkmjQJKWZ3vmezLSebtW3VRxKKH3n8=
|   256 5a:06:ed:eb:b6:56:7e:4c:01:dd:ea:bc:ba:fa:33:79 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGB22m99Wlybun7o/h9e6Ea/9kHMT0Dz2GqSodFqIWDi
80/tcp   open  http        syn-ack ttl 61 Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
| http-robots.txt: 1 disallowed entry 
|_/admin.html
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
111/tcp  open  rpcbind     syn-ack ttl 61 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100003 
```

### smp-share-enumerate

```text
Starting Nmap 7.91 ( https://nmap.org ) at 2021-06-17 17:35 IST
Stats: 0:00:55 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 0.00% done
Stats: 0:00:55 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 0.00% done
Stats: 0:00:56 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 50.00% done; ETC: 17:37 (0:00:53 remaining)
Stats: 0:00:56 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 50.00% done; ETC: 17:37 (0:00:53 remaining)
Stats: 0:00:56 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 50.00% done; ETC: 17:37 (0:00:54 remaining)
Nmap scan report for 10.10.213.207
Host is up (0.70s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.213.207\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: IPC Service (kenobi server (Samba, Ubuntu))
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.213.207\anonymous: 
|     warning: Couldn't get details for share: SMB: Failed to receive bytes: TIMEOUT
|     Type: Not a file share
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.213.207\print$: 
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\var\lib\samba\printers
|     Anonymous access: <none>
|_    Current user access: <none>

Nmap done: 1 IP address (1 host up) scanned in 131.61 seconds
```
