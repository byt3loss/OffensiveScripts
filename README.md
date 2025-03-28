# Offensive Scripts

A collection of scripts written by me or modified versions of others' scripts, categorized by target or attack technique.

## Index

### CVE Exploits

#### CVE-2025-45878

Chains and automates Arbitrary File Write to RCE on Gibbon LMS through [CVE-2023-45878](https://herolab.usd.de/security-advisories/usd-2023-0025/) exploitation.

The script performs the following steps:
1. Generates an msfvenom stageless reverse shell for Windows
2. Uploads a webshell exploiting CVE-2023-45878
3. Downloads the reverse shell on the target
4. Executes the reverse shell

Usage: `CVE-2025-45878.sh <lhost> <lport> <rhost[:rport]>`.

### Python Werkzeug

#### LFI_to_RCE

Exploits an LFI endpoint to read system files and generate the Werkzeug PIN.

#### SQLi_to_RCE 

Exploits SQLi to read system files and generate Werkzeug PIN (from TryHackMe Advent Of Cyber 2023 Side Quest 4)

### SSRF

#### SSRF_Scout

Tool to enumerate subdomains exposed locally thru a POST parameter vulnerable to SSRF. The script uses [RawHTTPy](https://pypi.org/project/rawhttpy/), a python package written by me to parse raw HTTP requests.
