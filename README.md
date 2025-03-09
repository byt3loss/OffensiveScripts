# Evil Scripts

A collection of scripts written by me or modified versions of others' scripts, categorized by target or attack technique.

## Index

### Python Werkzeug

#### LFI_to_RCE

Exploits an LFI endpoint to read system files and generate the Werkzeug PIN.

#### SQLi_to_RCE 

Exploits SQLi to read system files and generate Werkzeug PIN (from TryHackMe Advent Of Cyber 2023 Side Quest 4)

### SSRF

#### SSRF_Scout

Tool to enumerate subdomains exposed locally thru a POST parameter vulnerable to SSRF. The script uses [RawHTTPy](https://pypi.org/project/rawhttpy/), a python package written by me to parse raw HTTP requests.


