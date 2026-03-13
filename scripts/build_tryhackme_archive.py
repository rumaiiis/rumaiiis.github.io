#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import re
import shutil
import zipfile
import xml.etree.ElementTree as ET


SITE_ROOT = Path("/home/metallica/portfolio/rumaiiis.github.io")
THM_ROOT = Path("/home/metallica/portfolio/rms/tryhackme")
ROOMS_DIR = SITE_ROOT / "generated" / "tryhackme"
DATA_FILE = SITE_ROOT / "_data" / "tryhackme_rooms.json"
POSTS_DIR = SITE_ROOT / "_posts"

SEASONAL_SERIES = {
    "AdventOfCyber-2019": "Advent of Cyber 2019",
    "AdventOfCyber-2021": "Advent of Cyber 2021",
    "25Days-of-CyberSecurity": "Advent of Cyber 2020",
}

TITLE_OVERRIDES = {
    "VulnNet_Internal": "VulnNet Internal",
    "VulnUniversity": "VulnUniversity",
    "Wgel-CTF": "Wgel CTF",
    "CTF-collection-Vol.1": "CTF Collection Vol.1",
    "ColddBox_Easy": "ColddBox Easy",
    "Erit_securus_1": "Erit Securus 1",
    "XXR": "XXR",
    "LFI": "LFI",
    "SSRF": "SSRF",
    "OSI-Model": "OSI Model",
    "OhSINT": "OhSINT",
    "burp": "Burp",
    "blaster": "Blaster",
    "battery": "Battery",
    "hashing": "Hashing",
    "kenobi": "Kenobi",
    "tomghost": "Tomghost",
    "pickle-rick": "Pickle Rick",
    "linux-privesc": "Linux Privesc",
    "Fowsniff-CTF": "Fowsniff CTF",
    "Simple-CTF": "Simple CTF",
    "Wgel-CTF": "Wgel CTF",
    "Brooklyn-Nine-Nine": "Brooklyn Nine-Nine",
    "YearOfTheRabbit": "Year of the Rabbit",
}

CATEGORY_META = {
    "seasonal-events": {
        "title": "Seasonal Events",
        "description": "Advent of Cyber series and day-wise challenge tracks.",
    },
    "windows-ad": {
        "title": "Windows and AD",
        "description": "Windows exploitation, SMB paths, and Active Directory practice.",
    },
    "web-apps": {
        "title": "Web and App Security",
        "description": "Web exploitation, app flaws, and browser-facing attack paths.",
    },
    "linux-privesc": {
        "title": "Linux and PrivEsc",
        "description": "Linux footholds, enumeration, and privilege-escalation workflows.",
    },
    "recon-fundamentals": {
        "title": "Recon and Fundamentals",
        "description": "Core network, recon, cracking, and defensive tooling exercises.",
    },
    "challenge-labs": {
        "title": "Challenge Labs",
        "description": "Mixed labs, CTF-style boxes, and broader challenge collections.",
    },
}

WINDOWS_AD_ROOMS = {
    "Alfred",
    "AttacktiveDirectory",
    "blaster",
    "Blue",
    "HackPark",
    "Ice",
    "Steel-Mountain",
}

WEB_APP_ROOMS = {
    "Authenticate",
    "AvengersBlog",
    "Bolt",
    "burp",
    "Django",
    "GameZone",
    "Ignite",
    "Juice-Shop",
    "LFI",
    "Nax",
    "OWASP",
    "Source",
    "SSRF",
    "Upload-Vulnerabilities",
    "VulnUniversity",
    "WebEnumeration",
}

LINUX_PRIVESC_ROOMS = {
    "AgentSudo",
    "Archangel",
    "BasicPentesting",
    "BountyHacker",
    "Brooklyn-Nine-Nine",
    "ColddBox_Easy",
    "Cyborg",
    "EasyPeasy",
    "Fowsniff-CTF",
    "GamingServer",
    "kenobi",
    "LazyAdmin",
    "LinuxEnumeration",
    "linux-privesc",
    "Mr-Robot",
    "NerdHerd",
    "Notes",
    "pickle-rick",
    "Res",
    "RootMe",
    "Simple-CTF",
    "Skynet",
    "Startup",
    "Team",
    "TheCodCaper",
    "tomghost",
    "VulnNet_Internal",
    "Wgel-CTF",
    "YearOfTheRabbit",
}

RECON_FOUNDATIONS_ROOMS = {
    "CrackTheHash",
    "Hardening-Basics-1",
    "hashing",
    "JohnRipper",
    "Nessus",
    "NetSec-Challenge",
    "Ninja-Skills",
    "OhSINT",
    "OSI-Model",
    "Python",
    "ToolsRus",
    "Wireshark",
}

RESEARCH_SUMMARIES = {
    "AgentSudo": {
        "summary": "Typical public walkthrough flow for this room is: enumerate HTTP/FTP/SSH, manipulate the User-Agent header to reveal the hidden clue, brute-force or recover FTP access for Chris, extract hidden material from the image files with binwalk and steghide, recover James's SSH access, then abuse sudo misconfiguration tied to CVE-2019-14287 for privilege escalation.",
        "focus": ["HTTP header manipulation", "FTP access recovery", "steganography workflow", "SSH foothold", "sudo CVE-2019-14287"],
    },
    "VulnNet_Internal": {
        "summary": "Public walkthroughs and the official room description both point to this box being centered on internal-service enumeration. The common methodology is to enumerate SMB/NFS-style internal services, recover business files or service data, use those artifacts to discover additional internal access paths, and pivot from exposed internal resources to a local user shell before final privilege escalation.",
        "focus": ["internal service enumeration", "SMB/NFS data exposure", "artifact-driven enumeration", "pivoting to local access", "Linux privilege escalation"],
    },
    "Blue": {
        "summary": "Blue is generally solved by identifying legacy SMB exposure on Windows, validating the EternalBlue attack surface, gaining a shell through the SMB vulnerability path, and then performing standard post-exploitation to recover proof files and system-level access.",
        "focus": ["SMB enumeration", "EternalBlue", "Windows exploitation", "post-exploitation basics"],
    },
    "Brooklyn-Nine-Nine": {
        "summary": "Most walkthroughs for this room follow a lightweight Linux CTF path: enumerate FTP/SSH/HTTP, recover the note or credential hint, gain SSH access, check sudo rights, and escalate with the permitted binary through a GTFOBins-style technique.",
        "focus": ["FTP enumeration", "credential discovery", "SSH access", "sudo abuse"],
    },
    "Brute-It": {
        "summary": "The intended learning path is straightforward web and credential abuse: enumerate services, discover the admin surface, brute-force or recover access, process the RSA material, obtain a user shell, and escalate through the sudo configuration available on the host.",
        "focus": ["service enumeration", "web brute-force", "RSA key recovery", "sudo-based privesc"],
    },
    "kenobi": {
        "summary": "The standard Kenobi path is to enumerate SMB and NFS exposure, recover SSH key clues from the anonymous share, abuse the vulnerable ProFTPD copy commands to move the private key into a mountable location, log in over SSH, and finish with PATH hijacking against a SUID binary.",
        "focus": ["SMB share discovery", "NFS enumeration", "ProFTPD mod_copy abuse", "SSH key recovery", "PATH hijack via SUID"],
    },
    "BountyHacker": {
        "summary": "Public walkthroughs consistently solve Bounty Hacker by enumerating FTP, SSH, and HTTP, extracting a task list from exposed content, using the recovered wordlist against SSH, landing a low-privilege shell, and escalating with a sudo-allowed GTFOBins path.",
        "focus": ["multi-service enumeration", "artifact-based credential discovery", "SSH brute-force", "Linux privilege escalation"],
    },
    "EasyPeasy": {
        "summary": "Easy Peasy is usually approached as a staged Linux/web challenge: enumerate multiple HTTP surfaces, recover clues and hashes from hidden content, crack the supplied materials, pivot to SSH, and complete privilege escalation through a writable scheduled-task or weak automation path.",
        "focus": ["multi-port web enumeration", "hash cracking", "hidden content discovery", "SSH pivot", "cron or automation abuse"],
    },
    "Archangel": {
        "summary": "Archangel generally follows an LFI-to-shell path: enumerate the hosted content, identify the local file inclusion issue, abuse log or file-based execution to gain code execution, then escalate through misconfigurations left on the Linux host.",
        "focus": ["directory enumeration", "LFI validation", "log poisoning or file execution", "Linux post-exploitation"],
    },
    "AttacktiveDirectory": {
        "summary": "Attacktive Directory is usually solved as an AD enumeration and credential-abuse lab: identify the domain, enumerate valid users, discover AS-REP roastable accounts or sprayable credentials, pivot into SMB or remote-management access, and recover the domain proof material through standard Windows post-exploitation.",
        "focus": ["domain enumeration", "Kerberos user discovery", "AS-REP roasting or spraying", "SMB or remote access", "Windows post-exploitation"],
    },
    "Alfred": {
        "summary": "Alfred is typically solved by identifying the exposed Jenkins service, abusing script-console or build functionality for code execution, establishing a Windows shell, and then using token or privilege abuse techniques to escalate to SYSTEM.",
        "focus": ["Jenkins enumeration", "authenticated code execution", "Windows shell access", "privilege escalation to SYSTEM"],
    },
    "BasicPentesting": {
        "summary": "Basic Pentesting usually walks through classic Linux enumeration: discover SMB and web services, recover clues or usernames, brute-force or reuse credentials for SSH, then enumerate the user context to collect the final proof material.",
        "focus": ["SMB and web enumeration", "username discovery", "SSH credential attack", "post-login enumeration"],
    },
    "Bolt": {
        "summary": "Bolt commonly follows a lightweight CMS attack path: fingerprint the Bolt CMS instance, recover or brute-force valid access, abuse administrative functionality to obtain code execution, and then stabilize a shell on the Linux host.",
        "focus": ["CMS fingerprinting", "credential recovery", "admin-panel abuse", "Linux foothold"],
    },
    "ColddBox_Easy": {
        "summary": "ColddBox Easy is generally approached by enumerating WordPress, finding weak or reused credentials, leveraging the application for initial access, and then escalating locally through misconfiguration or exposed credential material on the box.",
        "focus": ["WordPress enumeration", "credential abuse", "web-to-shell workflow", "local privilege escalation"],
    },
    "Cyborg": {
        "summary": "Cyborg usually combines web enumeration with Borg backup recovery: enumerate the exposed application, retrieve archive or configuration material, crack or reuse recovered credentials, gain a local shell, and finish with Linux privilege escalation.",
        "focus": ["web enumeration", "backup artifact recovery", "credential cracking", "Linux privesc"],
    },
    "Fowsniff-CTF": {
        "summary": "Fowsniff centers on credential reuse from leaked data. The common path is to gather exposed user information, crack or test recovered passwords, gain shell access through a remote service, and escalate from the low-privilege Linux context.",
        "focus": ["OSINT-style data collection", "password cracking", "service login", "Linux privilege escalation"],
    },
    "GameZone": {
        "summary": "GameZone is usually solved by enumerating the login workflow, exploiting injection or weak validation in the web layer, recovering database-backed information, and using that access to transition into host-level compromise.",
        "focus": ["web login analysis", "injection testing", "database extraction", "web-to-host pivot"],
    },
    "HackPark": {
        "summary": "HackPark typically revolves around the BlogEngine.NET surface: identify the vulnerable web application, gain code execution or a web shell through the application, then use Windows enumeration and scheduled-task or service abuse to reach administrative access.",
        "focus": ["ASP.NET application enumeration", "web shell delivery", "Windows enumeration", "task or service abuse"],
    },
    "Ice": {
        "summary": "Ice commonly follows a Metasploit-oriented Windows workflow: identify the vulnerable media service, exploit the target to gain a session, migrate or stabilize access, and complete post-exploitation with privilege-focused enumeration.",
        "focus": ["service fingerprinting", "Metasploit exploitation", "session management", "Windows post-exploitation"],
    },
    "Ignite": {
        "summary": "Ignite is generally a Fuel CMS exploitation room. The normal path is to confirm the vulnerable CMS version, exploit the known RCE issue, establish a shell, harvest local credentials or configuration values, and then escalate on the Linux host.",
        "focus": ["Fuel CMS fingerprinting", "known RCE path", "shell establishment", "credential harvesting", "Linux privesc"],
    },
    "LazyAdmin": {
        "summary": "Lazy Admin usually starts with CMS enumeration and weak credential handling, then transitions into Linux shell access and a straightforward local privilege-escalation path using exposed scripts, writable files, or sudo misconfiguration.",
        "focus": ["CMS enumeration", "credential recovery", "Linux foothold", "local misconfiguration abuse"],
    },
    "HackPark": {
        "summary": "HackPark typically revolves around the BlogEngine.NET surface: identify the vulnerable web application, gain code execution or a web shell through the application, then use Windows enumeration and scheduled-task or service abuse to reach administrative access.",
        "focus": ["ASP.NET application enumeration", "web shell delivery", "Windows enumeration", "task or service abuse"],
    },
    "Mr-Robot": {
        "summary": "Mr Robot is typically solved by enumerating the web root and hidden files, recovering credentials from site content, logging into WordPress, abusing plugin or theme execution for a shell, and escalating locally after stabilizing access.",
        "focus": ["content discovery", "credential recovery", "WordPress abuse", "shell stabilization", "Linux privesc"],
    },
    "Ice": {
        "summary": "Ice commonly follows a Metasploit-oriented Windows workflow: identify the vulnerable media service, exploit the target to gain a session, migrate or stabilize access, and complete post-exploitation with privilege-focused enumeration.",
        "focus": ["service fingerprinting", "Metasploit exploitation", "session management", "Windows post-exploitation"],
    },
    "RootMe": {
        "summary": "Root Me usually follows a file-upload-to-shell path: enumerate the web application, bypass upload filtering, gain a shell on the host, and escalate through SUID or other local privilege-escalation opportunities.",
        "focus": ["web enumeration", "upload bypass", "web shell execution", "SUID enumeration"],
    },
    "Simple-CTF": {
        "summary": "Simple CTF generally involves standard Linux CTF methodology: enumerate web and SSH services, recover or brute-force credentials, obtain a foothold, and then escalate through locally exposed binaries, files, or sudo rights.",
        "focus": ["service enumeration", "credential recovery", "SSH foothold", "Linux privilege escalation"],
    },
    "Skynet": {
        "summary": "Skynet commonly combines SMB and web enumeration: discover accessible shares, recover credentials or hints, pivot through the application layer, gain shell access, and finish with a cron, script, or file-permission based privilege escalation path.",
        "focus": ["SMB enumeration", "credential discovery", "web pivot", "shell access", "Linux privesc"],
    },
    "Startup": {
        "summary": "Startup is typically solved by enumerating FTP and web services, identifying an upload or writable-content path, obtaining a reverse shell, and then escalating through local credentials, scripts, or scheduled tasks left on the system.",
        "focus": ["FTP enumeration", "web content abuse", "reverse shell", "local escalation workflow"],
    },
    "Team": {
        "summary": "Team generally follows a web-to-SSH Linux path: use web enumeration to recover hints or local file access, obtain credentials or a user foothold, transition into SSH, and escalate via writable scripts or trusted execution paths.",
        "focus": ["web enumeration", "file access abuse", "credential recovery", "SSH foothold", "Linux privesc"],
    },
    "TheCodCaper": {
        "summary": "The Cod Caper usually emphasizes methodical Linux enumeration: identify the exposed services, leverage the web surface for credentials or entry, obtain user access, and escalate through sudo or binary abuse after local inspection.",
        "focus": ["service discovery", "web-assisted foothold", "user access", "sudo or binary abuse"],
    },
    "Wgel-CTF": {
        "summary": "Wgel CTF is commonly approached through web directory discovery, username and SSH key recovery, access to a Linux user account, and local privilege escalation using misconfigured writable or executable paths.",
        "focus": ["directory enumeration", "SSH key discovery", "user shell", "Linux privesc"],
    },
    "YearOfTheRabbit": {
        "summary": "Year of the Rabbit typically blends web enumeration, hidden content discovery, weak credential handling, and Linux post-exploitation. The common flow is to pivot from the application layer to a shell and then enumerate carefully for the final escalation route.",
        "focus": ["web enumeration", "hidden-content discovery", "credential abuse", "Linux post-exploitation"],
    },
    "NerdHerd": {
        "summary": "Nerd Herd is generally approached through layered clue-chaining: combine web hints, FTP artifacts, and SMB enumeration to recover credentials, obtain a Linux foothold, and then escalate through local weaknesses uncovered during post-exploitation.",
        "focus": ["multi-service enumeration", "cipher or clue analysis", "SMB credential recovery", "Linux post-exploitation"],
    },
    "tomghost": {
        "summary": "Tomghost commonly begins with Tomcat and AJP enumeration. The usual path is to exploit the Ghostcat file-read issue, recover credential material from configuration files, pivot into SSH, and then escalate locally using accessible backup or key artifacts.",
        "focus": ["Tomcat enumeration", "Ghostcat or AJP abuse", "config-file credential recovery", "SSH pivot", "Linux privesc"],
    },
}

CURATED_ROOM_NOTES = {
    "AgentSudo": """## Recon

- Initial enumeration exposes three primary services: `ftp`, `ssh`, and `http`.
- The web layer contains the first pivot. Changing the `User-Agent` value reveals the hidden clue path and points toward the next user context.

## Initial Access

- After identifying the hidden hint on the web service, the workflow moves to FTP access recovery.
- Image artifacts in the FTP-accessible material contain the next secrets. The intended path uses `binwalk` and `steghide`-style extraction to recover embedded data.
- Those recovered secrets provide the bridge to the SSH foothold.

## Privilege Escalation

- Once the Linux user shell is established, local enumeration shows a permissive `sudo` configuration.
- The escalation path maps to `CVE-2019-14287`, where a sudo rule can be abused to execute commands as root despite an apparent restriction.

## Defensive Takeaway

- Treat client-controlled headers as untrusted, but remember they can still expose workflow clues or logic differences during testing.
- Hidden data in images and archives is a common challenge pattern and a good reminder to inspect artifacts, not just obvious files.
- Sudo policy edge cases remain high-value privilege-escalation findings on Linux systems.
""",
    "kenobi": """## Recon

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
""",
    "Simple-CTF": """## Recon

- The target exposes `ftp`, `http`, and `ssh` on a non-standard port.
- Directory enumeration on the web service identifies the `/simple` path, which points to the main application surface.
- Additional content discovery exposes the admin area and upload-related paths used during further testing.

## Initial Access

- The key application fingerprint is `CMS Made Simple`, and the room is commonly solved by validating the relevant SQL injection path against that version.
- Credential material recovered from the application and supporting files is then reused for SSH access.
- After the login succeeds, the low-privilege shell becomes the pivot for local enumeration.

## Privilege Escalation

- The local user has a useful `sudo` permission on `vim`.
- That leads to a direct `GTFOBins`-style escalation path and root shell access.

## Defensive Takeaway

- Directory enumeration still pays off against small CMS deployments because hidden admin panels and secondary paths often expose the real attack surface.
- Public CMS exploits become much more dangerous when paired with password reuse between the app and the operating system.
- Even narrow `sudo` allowances can become full compromise if the delegated binary supports shell escape.
""",
    "BountyHacker": """## Recon

- Initial enumeration exposes `ftp`, `ssh`, and `http`, which maps the room as a classic Linux multi-service target.
- Anonymous or weakly protected content on the exposed services leaks the task list and the first useful username context.

## Initial Access

- The recovered task list and password candidates point directly toward an SSH credential attack.
- The intended path is to validate the wordlist material against the user account and convert that into an SSH foothold.

## Privilege Escalation

- After landing the user shell, local enumeration reveals a sudo-allowed binary or command path that can be abused for escalation.
- The final step is a straightforward GTFOBins-style move from user to root.

## Defensive Takeaway

- Small operational notes can expose enough context to collapse the attacker’s enumeration time.
- Reused or weak credentials turn even a short wordlist into a practical remote-access path.
- Sudo delegation should always be reviewed with shell-escape paths in mind.
""",
    "EasyPeasy": """## Recon

- Service enumeration identifies multiple web surfaces and a non-standard SSH port, which signals a layered challenge rather than a single vulnerable app.
- Directory and content discovery are central to the room. Hidden paths and embedded clues reveal the flags, password material, and the route to the foothold.

## Initial Access

- The intended route is to recover and crack the exposed hash material using the wordlist context provided by the room artifacts.
- Once the credentials are recovered, they are reused against SSH to establish the user shell on the Linux host.

## Privilege Escalation

- Post-exploitation focuses on weak automation or writable scheduled-task behavior.
- The path to root is not about a kernel exploit; it is about careful local enumeration and abuse of the host’s automation workflow.

## Defensive Takeaway

- Multi-port web exposure increases the chance that a hidden or less-monitored application becomes the real point of compromise.
- Recoverable hashes are effectively credentials once an attacker has enough context to crack them.
- Cron jobs and writable automation paths remain one of the most common avoidable Linux privilege-escalation problems.
""",
    "Archangel": """## Recon

- The initial web surface looks ordinary, but directory discovery and hostname clues quickly show that the interesting path sits behind secondary content.
- `robots.txt` and development-facing pages provide the first pivot toward the vulnerable application behavior.

## Initial Access

- The core issue is local file inclusion on the development PHP endpoint.
- After validating file read, the next step is to convert that inclusion path into code execution through a file- or log-based technique and then stabilize a shell.

## Privilege Escalation

- Once code execution is established, the room moves into Linux post-exploitation.
- The escalation route depends on local misconfiguration and execution context rather than a public kernel exploit.

## Defensive Takeaway

- Development pages and test endpoints are often the weakest link in otherwise small web stacks.
- LFI should never be treated as “just file read” because it often becomes shell access when paired with writable logs or scriptable inputs.
- Tight application separation and controlled execution paths reduce the blast radius after web compromise.
""",
    "RootMe": """## Recon

- Enumeration exposes a straightforward web application and SSH, but the real attack surface is the upload functionality rather than remote login.
- Directory discovery highlights the panel used to submit files and the location where uploaded content becomes accessible.

## Initial Access

- The intended path is to bypass upload restrictions and land a PHP-based reverse shell on the host.
- Once the shell is active, the room shifts into basic Linux enumeration to collect proof artifacts and assess escalation paths.

## Privilege Escalation

- The main privilege-escalation clue is a SUID-enabled binary.
- Abusing the Python SUID path through a GTFOBins technique yields the root shell.

## Defensive Takeaway

- Upload validation must include extension handling, execution policy, and storage isolation or it becomes direct code execution.
- Web-to-shell compromise often happens long before defenders notice anything at the SSH layer.
- SUID misconfigurations are high-impact because they turn a basic foothold into full system compromise with minimal noise.
""",
    "Skynet": """## Recon

- Enumeration shows a richer service set than a normal boot-to-root box, including SMB and mail-facing services alongside HTTP.
- SMB access and mail content provide the key sources of operational clues, usernames, and password material.

## Initial Access

- The common path is to recover or brute-force Miles Dyson’s mailbox access, harvest the hidden CMS path and related credentials, and then pivot through the web application.
- From there, file-inclusion style abuse against the application is used to land a reverse shell on the Linux host.

## Privilege Escalation

- After the user shell is established, the final step depends on local file permissions, writable scripts, or scheduled execution paths.
- The escalation route is more about chaining recovered access cleanly than forcing a single complex exploit.

## Defensive Takeaway

- Shared secrets across SMB, mail, and web services make multi-service environments much easier to break than they appear from outside.
- Hidden application paths are not protection; they only delay discovery until enumeration catches up.
- Internal scripts and automation need the same hardening attention as public-facing services.
""",
    "Wgel-CTF": """## Recon

- Initial enumeration shows a simple Linux target, but the web content hides the real pivot inside the `sitemap` path.
- Further directory discovery inside that path exposes `.ssh` material and the user context needed for remote access.

## Initial Access

- The intended route is to recover the SSH private key associated with the exposed user and authenticate directly to the host.
- This turns content discovery into a full remote-login path without requiring password guessing.

## Privilege Escalation

- Local enumeration shows a permissive `sudo` rule for `wget`.
- That delegated binary can be abused to overwrite sensitive files or redirect privileged file operations, leading to root.

## Defensive Takeaway

- Publishing `.ssh` material under a web path is an immediate compromise condition, not a minor leakage issue.
- Key-based access is only stronger than passwords if the private key stays private.
- Even narrow `sudo` access to file-handling utilities like `wget` can be enough for full compromise.
""",
    "battery": """## Recon

- The portal exposes a minimal web surface, but directory discovery reveals administrative and reporting paths that matter more than the landing page.
- The downloaded reporting artifact becomes the first real lead because it leaks usernames and hints about the application’s trust model.

## Initial Access

- The intended path centers on application logic flaws rather than brute force alone.
- By abusing inconsistent username-length handling between registration and login, the room can be approached as a truncation-style authentication issue.
- After gaining administrative access, the XML-processing functionality opens the door to XXE-based file reads and further credential discovery.

## Privilege Escalation

- Once higher-privileged credentials are recovered from application files and configuration data, the attack shifts into host access and local privilege escalation.
- The final step is less about a single public exploit and more about chaining the trust failures already present in the application stack.

## Defensive Takeaway

- Validation differences between registration and login paths can become authentication bypass conditions.
- XML parsers with unsafe external-entity handling turn ordinary features into file-read and secret-extraction primitives.
- Hardcoded credentials inside application files collapse the gap between web compromise and system compromise.
""",
    "Bolt": """## Recon

- Service enumeration shows the normal web front and a second web service where the actual CMS is hosted.
- CMS fingerprinting quickly identifies Bolt and gives both the version context and the likely administrative attack surface.

## Initial Access

- The practical path is to recover or validate the exposed CMS credentials and log into the administrative interface.
- From there, the challenge pivots into authenticated remote code execution through the Bolt application rather than a public unauthenticated exploit path.

## Privilege Escalation

- Once code execution is available through the CMS, the remaining work is to stabilize the Linux shell and enumerate locally for proof material.
- The room emphasizes web-to-host compromise more than a separate complex root exploit.

## Defensive Takeaway

- Secondary application ports are often more important than the default website and should not be treated as less sensitive.
- CMS administrator access is already high-impact; patch lag and credential reuse make it even worse.
- Application admins should be isolated from operating-system trust wherever possible.
""",
    "Cyborg": """## Recon

- The exposed web paths reveal both administrative content and backup-related artifacts.
- The most valuable discovery is the Borg repository reference, which shifts the room from simple web enumeration into backup recovery.

## Initial Access

- The route to access is to extract the Borg archive with recovered credentials and mine the restored content for the next account secret.
- That recovered credential is then reused for SSH access to obtain the Linux foothold.

## Privilege Escalation

- After the SSH foothold, local enumeration drives the rest of the room.
- The box is designed to reward artifact analysis and credential recovery more than noisy exploitation.

## Defensive Takeaway

- Backup systems are highly sensitive because they frequently contain both data and operational secrets.
- Reusing credentials across backup tooling and user access paths multiplies the impact of a single leak.
- Publicly exposed administrative or backup content should be treated as a critical finding, not a misconfiguration footnote.
""",
    "Fowsniff-CTF": """## Recon

- The web surface, mail services, and SSH together make this a credential-centric challenge rather than a pure exploit room.
- Public-facing information and leaked employee data are the first practical source of access.

## Initial Access

- The common path is to recover the exposed credential material, crack or test the passwords, access the mailbox, and extract the temporary secret needed for remote login.
- That mailbox-to-SSH pivot is the core transition in the room.

## Privilege Escalation

- Once the low-privilege shell is in place, standard Linux enumeration reveals the privilege-escalation route.
- The challenge is designed around chaining leaked identity data into host compromise, not bypassing patched services.

## Defensive Takeaway

- User-data leaks remain dangerous because they often include just enough material for password recovery and mailbox compromise.
- Email access frequently unlocks the rest of the environment because it becomes the reset and secret-distribution channel.
- Credential hygiene and mailbox protection are part of infrastructure defense, not just user support.
""",
    "GameZone": """## Recon

- The visible application is the real attack surface, so the first step is to inspect login behavior and input handling rather than hunt for hidden services.
- SQL injection against the login or search workflow is the intended pivot into the backend data.

## Initial Access

- After authentication bypass or injection succeeds, the database content yields the hash and username needed for the next stage.
- Once the recovered secret is cracked, SSH access provides the Linux foothold.

## Privilege Escalation

- Post-login enumeration reveals an internally exposed management interface, typically Webmin, running in a way that can be leveraged locally.
- That local management surface is then used to escalate from user to root.

## Defensive Takeaway

- Authentication forms are high-value attack paths because a single injection flaw can hand over both app and host access.
- Database-backed secrets remain highly dangerous when users reuse them for SSH or administration.
- Local-only admin services are still critical exposure if an attacker can land even a basic shell first.
""",
    "LazyAdmin": """## Recon

- Web enumeration reveals the hidden CMS path quickly, and further content discovery exposes backup and include directories that leak credential material.
- The room rewards directory discovery more than exploit spraying; the data is already present if the paths are found.

## Initial Access

- The exposed backup data yields the administrative credentials for the CMS.
- After logging into the management panel, the intended path is to upload or place a PHP reverse shell and convert application access into a Linux shell.

## Privilege Escalation

- Once on the host, the privilege-escalation route depends on local scripts, weak trust boundaries, or sudo-assisted execution.
- The room is designed to show how quickly a “small” CMS issue becomes full compromise when secrets are exposed.

## Defensive Takeaway

- Backup files inside the web root are effectively credential disclosure.
- CMS admin panels should never have the ability to drop executable content without strict controls.
- Web compromise plus weak local execution rules is enough for total host loss on small Linux deployments.
""",
    "Mr-Robot": """## Recon

- The web root leaks a large amount of content, and hidden files plus WordPress indicators quickly identify the application stack.
- Username enumeration is practical because the login flow responds differently to invalid usernames and invalid passwords.

## Initial Access

- The intended route is to recover the valid WordPress username, then work through the `fsocity.dic` credential source to recover the password.
- Once authenticated, theme or template editing provides a direct path to PHP code execution and a reverse shell.

## Privilege Escalation

- After landing on the host, the next credential pivot comes from the restricted user material stored locally.
- The final step uses a SUID-enabled `nmap` binary to jump from the user context to root.

## Defensive Takeaway

- Login error messages should never help an attacker separate valid usernames from invalid ones.
- Web application admin access must be treated as near-host compromise when file editing or code execution is available.
- Old SUID-enabled tooling remains a direct privilege-escalation path on Linux systems.
""",
    "Team": """## Recon

- The visible site looks almost like a default Apache page, but the hostname clue in the title is the first real step in the room.
- Once the host entry is added, directory and virtual-host enumeration expose the useful application content and user context.

## Initial Access

- The room is solved by combining web clues, local-file-read behavior, and credential recovery rather than brute force alone.
- After the right user context is recovered, the path transitions into SSH for a stable Linux foothold.

## Privilege Escalation

- Post-exploitation focuses on writable scripts or trusted execution paths that run under a higher-privilege user.
- The box rewards careful inspection of local automation and delegated execution rather than noisy exploitation.

## Defensive Takeaway

- Small hostname clues can hide the real attack surface from casual testing, but not from structured enumeration.
- File-read issues frequently become credential compromise once application data and local scripts are exposed.
- Trusted scripts and scheduled execution paths need the same hardening attention as public-facing services.
""",
    "YearOfTheRabbit": """## Recon

- Initial web enumeration appears ordinary until the static content and media assets are inspected more closely.
- The room deliberately hides the useful path behind redirections, asset references, and content that only becomes obvious after interception and careful review.

## Initial Access

- The intended route is to recover the hidden directory from the web flow, extract the FTP username and password material from the staged artifact, and brute-force or validate FTP access.
- Further artifact analysis on the downloaded file yields the SSH credentials for the next user context.

## Privilege Escalation

- After the SSH foothold, local enumeration and the hidden `s3cr3t` clue expose the path to the next user and finally to root.
- The final escalation hinges on a vulnerable `sudo` path combined with an allowed editor or delegated command.

## Defensive Takeaway

- Static assets, redirects, and media files can leak as much as dynamic endpoints when attackers inspect them properly.
- Obscure encodings and esoteric formats are not protection; they only delay basic analysis.
- Old `sudo` edge cases and delegated editor access remain dangerous escalation primitives.
""",
    "NerdHerd": """## Recon

- This room expects the attacker to combine clues across web, FTP, and SMB instead of relying on a single service.
- The early hints come from source comments, encoded values, and leaked artifact names that only make sense after some decoding or pattern matching.

## Initial Access

- FTP and SMB enumeration provide the user context and the secret material needed to recover the working credentials.
- Once the share and clue chain are solved, SSH becomes the practical foothold into the Linux host.

## Privilege Escalation

- After login, local enumeration becomes the deciding factor.
- The final escalation depends on host weakness rather than application logic, and the room rewards thorough post-exploitation review.

## Defensive Takeaway

- Small clue leaks across multiple services often combine into a full credential path even if each single leak looks harmless.
- Shared secrets between SMB, FTP, and SSH reduce an attacker’s workload dramatically.
- Attackers only need one successful interpretation of a clue chain to turn soft exposure into root access.
""",
    "Startup": """## Recon

- The box exposes a small service set, but anonymous FTP access and the mirrored web content make the writable file path the real priority.
- The `/files` area quickly becomes the central pivot because it links the FTP exposure to web-reachable content.

## Initial Access

- The intended path is to upload a web shell or command-capable payload through the writable FTP area and trigger it over HTTP.
- That provides the first host-level foothold without needing SSH credentials up front.

## Privilege Escalation

- During local enumeration, the packet capture becomes the source of the user credential, which moves the shell into a stronger user context.
- The final step depends on identifying a root-owned automation path and replacing or influencing the script it executes.

## Defensive Takeaway

- Anonymous writable FTP plus web-served content is effectively remote code execution waiting to happen.
- Internal network captures often leak much more than intended, including passwords and workflow clues.
- Root cron jobs should never execute user-controlled scripts or files.
""",
    "tomghost": """## Recon

- Service enumeration immediately highlights Tomcat and AJP, which is the real attack surface rather than the SSH service.
- The Tomcat version and exposed AJP port are the key indicators that the host is vulnerable to Ghostcat-style file disclosure.

## Initial Access

- The intended route is to abuse the AJP connector to read sensitive files from the Tomcat application context.
- Recovered credentials or key material are then reused to obtain SSH access and establish the Linux foothold.

## Privilege Escalation

- Once on the host, the room shifts into artifact-driven Linux escalation.
- Backup or private-key material left on disk provides the next pivot, and local trust relationships complete the final move to root.

## Defensive Takeaway

- AJP should not be exposed broadly, especially on older Tomcat deployments.
- Configuration and backup files often hold enough secrets to turn a file-read bug into full host access.
- Host cleanup matters: stale keys and archived materials remain dangerous long after the original service issue is patched.
""",
    "Alfred": """## Recon

- Initial enumeration highlights two important web services: the default IIS site and a Jenkins instance on the alternate HTTP port.
- Jenkins is the true attack surface here, and the exposed service immediately suggests a CI/CD-driven compromise path rather than a classic Windows service exploit.

## Initial Access

- The practical route is to authenticate to Jenkins and abuse job execution or script-console style functionality to run commands on the host.
- That yields the first Windows shell and turns the room into a post-exploitation exercise.

## Privilege Escalation

- The escalation step relies on Windows token context and privilege abuse rather than a network exploit.
- Once the session is stabilized, the attacker can impersonate or leverage a higher-privileged token to reach `SYSTEM`.

## Defensive Takeaway

- CI/CD platforms are high-impact assets because build execution is effectively remote code execution by design.
- Alternate admin ports should be treated as core production exposure, not “secondary” services.
- Windows privilege token abuse is a reminder that post-exploitation hardening matters after the initial compromise.
""",
    "AttacktiveDirectory": """## Recon

- This room is centered on Active Directory rather than a single host exploit, so the first step is domain and user enumeration.
- Kerberos, SMB, and other AD-facing services provide enough signal to identify the domain structure and likely attack paths.

## Initial Access

- The intended route is to enumerate valid users, identify weak credential opportunities, and abuse Kerberos-based weaknesses such as AS-REP roasting or password spraying.
- Once valid credentials are recovered, the room pivots into domain-aware access and proof collection.

## Privilege Escalation

- The privilege-escalation phase is more about expanding domain access and reading the right protected material than forcing a single exploit.
- Standard AD post-exploitation workflow and careful enumeration lead to the final flags.

## Defensive Takeaway

- User enumeration and Kerberos abuse remain highly effective against weakly hardened domains.
- Good password policy, pre-auth enforcement, and account monitoring materially reduce the success rate of these workflows.
- Small AD hygiene failures compound quickly because every recovered identity expands the attacker’s graph.
""",
    "Blue": """## Recon

- The most important discovery is legacy SMB exposure on a Windows host with the right version profile for `MS17-010`.
- Vulnerability validation confirms that the box is built around the EternalBlue attack path.

## Initial Access

- The intended route is to exploit the SMB service and obtain a shell through the EternalBlue chain.
- Once code execution lands, the rest of the room shifts into straightforward Windows post-exploitation.

## Privilege Escalation

- The exploit itself effectively provides a high-privilege context, so the remaining work is to stabilize access and recover the proof material.
- The box is designed to teach the exploitation chain and the basic post-exploitation workflow that follows.

## Defensive Takeaway

- Legacy SMB exposure remains one of the clearest examples of how a single unpatched service can become full host compromise.
- Network segmentation and aggressive patching are still the most important defenses against exploit chains like EternalBlue.
- Even training boxes like this highlight why old Windows attack surface should be retired or isolated quickly.
""",
    "HackPark": """## Recon

- The IIS-hosted web application is the main attack surface, and the login workflow is the first area to examine closely.
- BlogEngine.NET indicators and the administrative path make it clear that the box is built around application compromise rather than direct RDP abuse.

## Initial Access

- The room is commonly solved by recovering or brute-forcing the blog credentials and then abusing the vulnerable BlogEngine.NET path to execute code.
- That provides the initial Windows foothold and moves the workflow into system enumeration.

## Privilege Escalation

- Once on the host, the path to administrative access depends on Windows task or service behavior and artifact-driven enumeration.
- The room rewards stable shell management and careful Windows host review after the web compromise.

## Defensive Takeaway

- Web applications on Windows hosts collapse the gap between app compromise and system compromise when upload or code-execution features are exposed.
- Password quality still matters even when the final exploit chain relies on a specific application bug.
- Task and service hardening are critical because they often become the second-stage privilege-escalation path.
""",
    "Ice": """## Recon

- Service fingerprinting identifies the vulnerable media service and quickly points toward a known exploit path.
- This room is intentionally oriented toward exploit selection and Metasploit workflow rather than manual vulnerability development.

## Initial Access

- The intended route is to use the compatible exploit module to gain a session on the Windows host.
- After that initial compromise, session handling, migration, and stabilization become the main focus.

## Privilege Escalation

- Post-exploitation relies on Windows enumeration and session management rather than a separate complex exploit.
- The room emphasizes the operator workflow after compromise as much as the exploit itself.

## Defensive Takeaway

- Outdated desktop or media services can become remote access paths just as easily as server software.
- Exploitability matters, but so does what an attacker can do with the first session they obtain.
- Endpoint hardening and service minimization are still the simplest ways to reduce this type of exposure.
""",
    "VulnNet_Internal": """## Recon

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
""",
}

CATEGORY_BRIEFS = {
    "seasonal-events": "Seasonal challenge series with day-wise tasks and broad topic coverage across offensive and defensive skills.",
    "windows-ad": "Windows-focused room covering network service enumeration, exploitation, lateral movement concepts, or Active Directory workflow.",
    "web-apps": "Web-facing lab centered on application testing, content discovery, misconfiguration abuse, and foothold development.",
    "linux-privesc": "Linux boot-to-root style room focused on service enumeration, foothold development, and privilege escalation paths.",
    "recon-fundamentals": "Skill-building room for reconnaissance, tooling, cracking, packet analysis, or security fundamentals.",
    "challenge-labs": "General mixed challenge room blending enumeration, exploitation, and post-exploitation practice.",
}

NOTE_FILE_PATTERNS = (
    "nmap",
    "gobuster",
    "dirb",
    "hydra",
    "wpscan",
    "ffuf",
    "nikto",
    "sqlmap",
    "enum",
    "scan",
    "report",
    "log",
    "request",
    "service",
    "business",
    "data",
)

SKIP_FILE_PATTERNS = (
    ".swp",
    ".zip",
    ".rar",
    ".png.extracted",
)

SENSITIVE_NAME_PATTERNS = (
    "flag",
    "pass",
    "password",
    "creds",
    "cred",
    "hash",
    "rsa",
    "id_rsa",
    "key",
    "shadow",
    "passwd",
    "ssh",
)

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

TEXT_REPLACEMENTS = {
    "hhtp": "http",
    "userAget": "User-Agent",
    "Annoucement": "Announcement",
    "togheter": "together",
    "you'te": "you're",
}


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def titleize(value: str) -> str:
    if value in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[value]
    value = value.replace("-", " ").replace("_", " ").strip()
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", value)
    value = re.sub(r"\s+", " ", value)
    return value.title()


def categorize_room(name: str, kind: str) -> str:
    if kind == "series":
        return "seasonal-events"
    if name in WINDOWS_AD_ROOMS:
        return "windows-ad"
    if name in WEB_APP_ROOMS:
        return "web-apps"
    if name in LINUX_PRIVESC_ROOMS:
        return "linux-privesc"
    if name in RECON_FOUNDATIONS_ROOMS:
        return "recon-fundamentals"
    return "challenge-labs"


def is_sensitive_name(name: str) -> bool:
    lowered = name.lower()
    return any(part in lowered for part in SENSITIVE_NAME_PATTERNS)


def sanitize_text(text: str) -> str:
    sanitized = text
    sanitized = re.sub(r"THM\{[^}]+\}", "[redacted challenge flag]", sanitized)
    sanitized = re.sub(r"root\.txt\s*[:=-]?\s*\S+", "root.txt: [redacted challenge flag]", sanitized, flags=re.I)
    sanitized = re.sub(r"user\.txt\s*[:=-]?\s*\S+", "user.txt: [redacted challenge flag]", sanitized, flags=re.I)
    sanitized = re.sub(r"password\s*[:=-]\s*\S+", "password: [redacted sensitive value]", sanitized, flags=re.I)
    sanitized = re.sub(r"passphrase\s*[:=-]\s*\S+", "passphrase: [redacted sensitive value]", sanitized, flags=re.I)
    sanitized = re.sub(r"\bWhat isn\b", "What is", sanitized, flags=re.I)
    sanitized = re.sub(r"\bHow you redirect yourself\b", "How do you redirect yourself", sanitized, flags=re.I)
    sanitized = re.sub(r"\bWhat is[n']t\b", "What is", sanitized, flags=re.I)
    for bad, good in TEXT_REPLACEMENTS.items():
        sanitized = sanitized.replace(bad, good)
    return sanitized


def sanitize_block(block_text: str, context: str) -> str:
    lowered = context.lower()
    sensitive = any(
        key in lowered
        for key in (
            "flag",
            "password",
            "passphrase",
            "credential",
            "creds",
            "root.txt",
            "user.txt",
            "agent name",
            "who is",
        )
    )
    block_text = sanitize_text(block_text)
    if sensitive:
        if "flag" in lowered or "root.txt" in lowered or "user.txt" in lowered:
            return "[redacted challenge flag]"
        return "[redacted sensitive answer]"
    return block_text.strip()


def extract_docx_text(path: Path) -> str:
    try:
        with zipfile.ZipFile(path) as zf:
            xml_data = zf.read("word/document.xml")
    except Exception:
        return ""

    try:
        root = ET.fromstring(xml_data)
        paragraphs: list[str] = []
        for para in root.findall(".//w:p", NS):
            texts = [node.text or "" for node in para.findall(".//w:t", NS)]
            line = "".join(texts).strip()
            if line:
                paragraphs.append(line)
        text = "\n".join(paragraphs)
        if text.strip():
            return text
    except ET.ParseError:
        pass

    matches = re.findall(rb"<w:t[^>]*>(.*?)</w:t>", xml_data, flags=re.DOTALL)
    parts: list[str] = []
    for match in matches:
        piece = match.decode("utf-8", "ignore")
        piece = (
            piece.replace("&amp;", "&")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
            .replace("&quot;", '"')
            .replace("&apos;", "'")
        )
        if piece.strip():
            parts.append(piece.strip())
    return "\n".join(parts)


def read_note_file(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        return extract_docx_text(path)
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def collect_files(folder: Path) -> tuple[list[Path], list[Path], list[Path]]:
    markdowns: list[Path] = []
    docs: list[Path] = []
    notes: list[Path] = []
    for path in sorted(folder.rglob("*")):
        if not path.is_file():
            continue
        name = path.name
        if any(pat in name for pat in SKIP_FILE_PATTERNS):
            continue
        if path.suffix.lower() == ".md" and name == "README.md":
            markdowns.append(path)
        elif path.suffix.lower() == ".docx":
            docs.append(path)
        elif path.suffix.lower() in {"", ".txt", ".log", ".nmap", ".gnmap", ".xml"}:
            lowered = name.lower()
            if any(token in lowered for token in NOTE_FILE_PATTERNS):
                notes.append(path)
    return markdowns, docs, notes


def normalize_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n").strip()
    lines = [line.rstrip() for line in text.splitlines()]
    out: list[str] = []
    in_block = False
    block: list[str] = []
    current_context = ""
    last_heading = ""

    for raw in lines:
        stripped = raw.strip()
        if re.fullmatch(r"'{2,}", stripped):
            if in_block:
                content = sanitize_block("\n".join(block).strip(), current_context)
                out.extend(["```text", content or "[redacted or empty block]", "```"])
                in_block = False
                block = []
            else:
                in_block = True
            continue
        if in_block:
            block.append(raw)
            continue
        if not stripped:
            out.append("")
            continue
        if re.fullmatch(r"[-=]{4,}.*[-=]{4,}", stripped):
            title = re.sub(r"[-=]{2,}", "", stripped).strip()
            if title:
                out.append(f"## {title}")
                current_context = title
            continue
        if re.match(r"^#\s*task", stripped, flags=re.I):
            if last_heading != "## Tasks":
                out.append("## Tasks")
                last_heading = "## Tasks"
            current_context = "Tasks"
            continue
        if re.fullmatch(r"task\s*\d+.*", stripped.lower()):
            heading = f"## {stripped.title()}"
            if last_heading != heading:
                out.append(heading)
                last_heading = heading
            current_context = stripped
            continue
        if stripped.lower() == "nmap":
            if last_heading != "## Recon Snapshot":
                out.append("## Recon Snapshot")
                last_heading = "## Recon Snapshot"
            current_context = "Recon Snapshot"
            continue
        if re.match(r"^\d+\.\s+", stripped):
            item = re.sub(r"^\d+\.\s+", "", stripped)
            out.append(f"- {item}")
            current_context = item
            continue
        if stripped.endswith("?") and len(stripped) < 120:
            out.append(f"- {sanitize_text(stripped)}")
            current_context = stripped
            continue
        out.append(sanitize_text(raw))
        current_context = stripped

    if in_block and block:
        content = sanitize_block("\n".join(block).strip(), current_context)
        out.extend(["```text", content or "[redacted or empty block]", "```"])

    cleaned = "\n".join(out)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
    return cleaned


def synthesize_room_notes(name: str, category: str) -> str:
    title = titleize(name)
    summary = RESEARCH_SUMMARIES.get(name)

    if summary:
        focus = summary["focus"]
        initial = ", ".join(focus[:2]) if len(focus) >= 2 else focus[0]
        privesc = ", ".join(focus[2:4]) if len(focus) >= 4 else ", ".join(focus[-2:])
        return (
            "## Recon\n\n"
            f"- {title} is best approached through structured enumeration rather than noisy exploitation.\n"
            f"- The early workflow usually centers on {initial}, which exposes the route into the room.\n\n"
            "## Initial Access\n\n"
            f"- The intended foothold comes from following the attack path described in the room flow and validating the exposed service behavior.\n"
            f"- In practice, this means converting the discovered clues into working access through {focus[0]} and adjacent enumeration findings.\n\n"
            "## Privilege Escalation\n\n"
            f"- After the first foothold, the room shifts into post-exploitation and local review.\n"
            f"- The key escalation themes are {privesc}, which complete the move to the final proof material.\n\n"
            "## Defensive Takeaway\n\n"
            f"- {title} reinforces how small exposure points compound when enumeration is disciplined and service relationships are understood.\n"
            "- The defensive lesson is to reduce credential reuse, remove unnecessary trust paths, and harden secondary services before they become the pivot."
        )

    category_templates = {
        "windows-ad": (
            "Windows and domain-facing services are the core focus of this room, so careful service enumeration sets the direction early.",
            "The initial foothold usually comes from weak authentication, service abuse, or an exposed administrative surface on the Windows host.",
            "Privilege escalation depends on Windows post-exploitation, token context, or local service and task behavior.",
            "The main lesson is that Windows management surfaces and legacy services must be hardened because one foothold often becomes full host control quickly.",
        ),
        "web-apps": (
            "The web application is the main attack surface, so content discovery, login behavior, and hidden paths matter immediately.",
            "The intended foothold comes from chaining application flaws, exposed content, or weak credentials into code execution or authenticated access.",
            "Once the app is compromised, the next step is to stabilize host access and enumerate for the final path to proof material.",
            "The defensive lesson is that web compromise rarely stays in the web tier when secrets, upload paths, or admin functions are exposed.",
        ),
        "linux-privesc": (
            "This room follows the usual Linux boot-to-root pattern where service enumeration and artifact review reveal the access path.",
            "The initial foothold comes from exposed services, leaked files, or weak credentials rather than blind exploitation.",
            "Privilege escalation depends on local enumeration, trust abuse, writable automation, or delegated execution paths on the host.",
            "The defensive lesson is that Linux post-exploitation paths are usually avoidable with better secret handling and tighter local permissions.",
        ),
        "recon-fundamentals": (
            "This room is more about methodology than a single exploit, so the emphasis is on disciplined reconnaissance and tool use.",
            "The useful progress comes from reading the environment correctly and validating the output of the relevant security tooling.",
            "If host access is part of the path, the post-exploitation steps are typically lightweight and focused on proof recovery rather than heavy exploitation.",
            "The defensive lesson is that information exposure and weak operational practice often matter just as much as software vulnerabilities.",
        ),
        "challenge-labs": (
            "This room mixes discovery, analysis, and exploitation, so the right path usually appears only after multiple clues are combined.",
            "Initial access depends on linking those clues together rather than relying on a single obvious vulnerability.",
            "After the foothold, the room transitions into standard host enumeration and local privilege-escalation review.",
            "The defensive lesson is that seemingly minor leaks across different services often combine into full compromise when an attacker is systematic.",
        ),
    }

    recon, access, privesc, takeaway = category_templates[category]
    return (
        "## Recon\n\n"
        f"- {recon}\n"
        f"- {title} rewards careful note-taking and stepwise validation rather than trial-and-error execution.\n\n"
        "## Initial Access\n\n"
        f"- {access}\n"
        f"- The room path becomes clear once the recovered artifacts and service behavior are linked together.\n\n"
        "## Privilege Escalation\n\n"
        f"- {privesc}\n"
        f"- After the foothold, local context matters more than noisy exploitation.\n\n"
        "## Defensive Takeaway\n\n"
        f"- {takeaway}"
    )


def build_body(folder: Path, kind: str) -> str:
    markdowns, docs, notes = collect_files(folder)
    name = folder.name
    title = SEASONAL_SERIES.get(name, titleize(name))
    body: list[str] = []
    body.append('<section class="page-hero panel">')
    body.append(f'  <p class="eyebrow">root@rumais:~# inspect {slugify(name)}</p>')
    body.append(f"  <h1>{title}</h1>")
    if kind == "series":
        body.append(f"  <p>Series archive for {title}. Use this as a structured entry point into the seasonal challenge notes and day-wise writeups.</p>")
    else:
        room_category = categorize_room(name, kind)
        brief = CATEGORY_BRIEFS[room_category]
        body.append(f"  <p>{brief} This page consolidates local notes, recovered artifacts, and cleaned-up workflow guidance with sensitive answers and flags redacted.</p>")
    body.append("</section>\n")

    if kind == "series":
        body.append('{% assign series_posts = site.posts | where: "series", page.series_name %}')
        body.append('<section class="panel">')
        body.append('  <h2>Day Index</h2>')
        body.append('  <div class="writeup-list">')
        body.append('  {% for post in series_posts %}')
        body.append('    <article class="writeup-card">')
        body.append('      <span class="writeup-label">Seasonal</span>')
        body.append('      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>')
        body.append('      <p class="writeup-meta">{{ post.event_day }}</p>')
        body.append('      <p>{{ post.excerpt | strip_html | truncate: 160 }}</p>')
        body.append('    </article>')
        body.append('  {% endfor %}')
        body.append('  </div>')
        body.append('</section>')
        return "\n".join(body) + "\n"

    room_category = categorize_room(name, kind)
    room_category_title = CATEGORY_META[room_category]["title"]

    body.append('<section class="panel">')
    body.append('  <h2>Room Profile</h2>')
    status = "Primary writeup exists in local notes" if markdowns else "Built from supporting notes and artifacts" if docs or notes else "Waiting for deeper manual reconstruction"
    body.append(f"  <p>{status}. This room is grouped under <strong>{room_category_title}</strong>.</p>")
    meta: list[str] = []
    if markdowns:
        meta.append(f"{len(markdowns)} markdown source")
    if docs:
        meta.append(f"{len(docs)} docx note")
    if notes:
        meta.append(f"{len(notes)} command artifact")
    if meta:
        body.append('  <div class="tag-list">')
        body.append(f'    <span class="tag">{room_category_title}</span>')
        for item in meta:
            body.append(f'    <span class="tag">{item}</span>')
        body.append('  </div>')
    body.append('</section>\n')

    if name in RESEARCH_SUMMARIES:
        summary = RESEARCH_SUMMARIES[name]
        body.append('<section class="panel">')
        body.append('  <h2>Attack Path Overview</h2>')
        body.append(f"  <p>{summary['summary']}</p>")
        body.append('  <div class="tag-list">')
        for item in summary["focus"]:
            body.append(f'    <span class="tag">{item}</span>')
        body.append('  </div>')
        body.append('</section>\n')
    else:
        body.append('<section class="panel">')
        body.append('  <h2>Workflow Focus</h2>')
        body.append(f"  <p>{CATEGORY_BRIEFS[room_category]} Use the recovered artifacts below as the evidence base for enumeration, access development, and post-exploitation review.</p>")
        body.append('</section>\n')

    if name in CURATED_ROOM_NOTES:
        body.append("## Operator Notes\n")
        body.append(CURATED_ROOM_NOTES[name].strip())
    elif kind == "room":
        body.append("## Operator Notes\n")
        body.append(synthesize_room_notes(name, room_category))
    elif markdowns:
        main_text = normalize_markdown(read_note_file(markdowns[0]))
        body.append("## Operator Notes\n")
        body.append(main_text)

    safe_docs = [p for p in docs if not is_sensitive_name(p.name) and p.name.lower() != "readme.docx"]
    if docs and not markdowns and name not in CURATED_ROOM_NOTES and kind != "room":
        readme_docx = next((p for p in docs if p.name.lower() == "readme.docx"), None)
        readme_text = ""
        if readme_docx:
            readme_text = normalize_markdown(sanitize_text(read_note_file(readme_docx))).strip()
        if readme_text:
            body.append("## Operator Notes\n")
            body.append(readme_text)

    if safe_docs:
        body.append("\n## Supporting Notes\n")
        for doc in safe_docs[:6]:
            text = normalize_markdown(sanitize_text(read_note_file(doc))).strip()
            if not text:
                continue
            body.append(f"### {doc.stem.replace('_', ' ').replace('-', ' ').title()}\n")
            body.append(text[:2500])
            body.append("")

    if notes:
        body.append("## Evidence Pack\n")
        for note in notes[:8]:
            content = sanitize_text(read_note_file(note)).strip()
            if not content:
                continue
            body.append(f"### {note.name}\n")
            body.append("```text")
            body.append(content[:2000])
            body.append("```")
            body.append("")

    if not markdowns and not docs and not notes:
        body.append("## Status\n")
        body.append("Manual writeup expansion is still pending. The folder currently contains limited or non-text artifacts, so this page is holding the room position in the archive until the workflow notes are rebuilt.\n")

    return "\n".join(body).strip() + "\n"


def room_front_matter(name: str, kind: str) -> str:
    slug = slugify(name)
    title = titleize(name)
    if kind == "series":
        series_name = SEASONAL_SERIES[name]
        return (
            "---\n"
            "layout: page\n"
            f'title: "/{slug}"\n'
            f'permalink: "/writeups/tryhackme/{slug}/"\n'
            'platform: "TryHackMe"\n'
            'writeup_type: "series"\n'
            f'series_name: "{series_name}"\n'
            "---\n\n"
        )
    return (
        "---\n"
        "layout: page\n"
        f'title: "/{slug}"\n'
        f'permalink: "/writeups/tryhackme/{slug}/"\n'
        'platform: "TryHackMe"\n'
        'writeup_type: "room"\n'
        f'room_name: "{title}"\n'
        "---\n\n"
    )


def build_inventory() -> list[dict]:
    rooms: list[dict] = []
    top_dirs = sorted([p for p in THM_ROOT.iterdir() if p.is_dir()], key=lambda p: p.name.lower())
    for folder in top_dirs:
        kind = "series" if folder.name in SEASONAL_SERIES else "room"
        markdowns, docs, notes = collect_files(folder)
        coverage = "full" if markdowns else "partial" if docs or notes else "stub"
        category = categorize_room(folder.name, kind)
        rooms.append(
            {
                "name": folder.name,
                "display_name": SEASONAL_SERIES.get(folder.name, titleize(folder.name)),
                "slug": slugify(folder.name),
                "kind": kind,
                "coverage": coverage,
                "category": category,
                "category_title": CATEGORY_META[category]["title"],
                "category_description": CATEGORY_META[category]["description"],
                "markdown_count": len(markdowns),
                "docx_count": len(docs),
                "note_count": len(notes),
                "url": f"/writeups/tryhackme/{slugify(folder.name)}/",
            }
        )
    return rooms


def write_inventory(rooms: list[dict]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(rooms, indent=2), encoding="utf-8")


def clean_room_posts() -> None:
    if not POSTS_DIR.exists():
        return
    for post in POSTS_DIR.glob("*.md"):
        text = post.read_text(encoding="utf-8", errors="ignore")
        if 'platform: "TryHackMe"' in text and 'writeup_type: "room"' in text:
            post.unlink()


def build_pages(rooms: list[dict]) -> None:
    if ROOMS_DIR.exists():
        shutil.rmtree(ROOMS_DIR)
    ROOMS_DIR.mkdir(parents=True, exist_ok=True)
    for room in rooms:
        folder = THM_ROOT / room["name"]
        target = ROOMS_DIR / f'{room["slug"]}.md'
        body = build_body(folder, room["kind"])
        target.write_text(room_front_matter(room["name"], room["kind"]) + body, encoding="utf-8")


def main() -> None:
    rooms = build_inventory()
    write_inventory(rooms)
    clean_room_posts()
    build_pages(rooms)
    print(f"generated {len(rooms)} room/series pages")


if __name__ == "__main__":
    main()
