# SSRF Rabbit Store

I developed these scripts while solving THM's Rabbit Store CTF.

The vulnerability consists in a misconfigured API endpoint that lets users activate their account just by adding the field `"subscription":"active"` when registering a new account.

```json
{"email":"user@gmail.com","password":"password", "subscription":"active"}
```

Once authenticated, the user can upload files from the device or an URL. The form is vulnerable to SSRF.

The scripts `port_scanner.sh` and `dir_scanner.sh` were developed to automate the exploit and find internal web services and their paths.

## Usage

### Automated exploit workflow

Automate account creation (`-r`), obtain a token and send payloads to the SSRF vulnerable form (`-u`).  

```sh
./ssrf.sh -r -u http://localhost/
```

Remove the `-r` flag if you have already registered an account.

### Internal port scanning

Exploit the SSRF vulnerability to scan for internal services.

```sh
./port_scan.sh
```

Note: Update the hardcoded token. 

Note 2: the script is designed to scan from port 80 to port 10000. Update the script if needed.


### Directory enumeration

Once you have found an internal web service, you may need to perform a directory enumeration.

```sh
./dir_scanner.sh -w dir.list
```

Note: Update the hardcoded token. 
