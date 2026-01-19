# Offensive Scripts

A collection of scripts written by me or modified versions of others' scripts, categorized by target or attack technique.

## Index


<details>
<summary><b>CVE Exploits</b></summary>

#### CVE-2023-45878

Chains and automates Arbitrary File Write to RCE on Gibbon LMS through [CVE-2023-45878](https://herolab.usd.de/security-advisories/usd-2023-0025/) exploitation.

The script performs the following steps:
1. Generates an msfvenom stageless reverse shell for Windows
2. Uploads a webshell exploiting CVE-2023-45878
3. Downloads the reverse shell on the target
4. Executes the reverse shell

Usage: `CVE-2023-45878.sh <lhost> <lport> <rhost[:rport]>`.

#### [CVE-2025-24893](/CVE_Exploits/CVE-2025-24893/)

Exploits XWiki RCE vulnerability and spawns a reverse shell on the target.

</details>

<details>
<summary><b>Python Werkzeug</b></summary>

#### [LFI to RCE](/Python_Werkzeug/LFI_to_RCE/)

Exploits an LFI endpoint to read system files and generate the Werkzeug PIN.

#### [SQLi to RCE ](/Python_Werkzeug/SQLi_to_RCE/)

Exploits SQLi to read system files and generate Werkzeug PIN (from TryHackMe Advent Of Cyber 2023 Side Quest 4)

</details>

<details>
<summary><b>SSRF</b></summary>

#### [SSRF Local Subdomains Enumeration](/SSRF/SSRF_subdomains_enum/)

Tool to enumerate subdomains exposed locally thru a POST parameter vulnerable to SSRF. The script uses [RawHTTPy](https://pypi.org/project/rawhttpy/), a python package written by me to parse raw HTTP requests.

#### [SSRF RabbitStore CTF](/SSRF/SSRF_RabbitStore_CTF/)

Three Bash scripts exploiting an SSRF vulnerability in the THM's RabbitStore CTF.

- **Automated exploit workflow** – [ssrf.sh](/SSRF/SSRF_RabbitStore_CTF/ssrf.sh): from account creation to SSRF payload delivery
- **Internal port scanning** - [port_scanner.sh](/SSRF/SSRF_RabbitStore_CTF/port_scanner.sh): discover internal web services via SSRF
- **Directory enumeration** - [dir_scanner.sh](/SSRF/SSRF_RabbitStore_CTF/dir_scanner.sh): brute-force directories on an internal service through SSRF

</details>

<details>
<summary><b>Others</b></summary>

#### [Gavel RCE](/Others/Gavel_RCE/README.md)

RCE exploitation automation for HackTheBox's [Gavel](https://app.hackthebox.com/machines/Gavel) CTF. Drops a web shell on the target for more command execution freedom, then spawns a mkfifo reverse shell through it.

#### [pyAesCrypt - brute-forcer](/Others/pyAesCrypt_bruteforcer/README.md)

Script to brute-force pyAesCrypt-encrypted files.

</details>
