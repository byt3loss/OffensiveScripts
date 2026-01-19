# pyAesCrypt - brute-forcer

This script was developed to brute-force a pyAesCrypt-encrypted ZIP file during HackTheBox [Imagery](https://app.hackthebox.com/machines/Imagery) CTF.

```sh
# install
virtualenv .venv
source .venv/bin/activate
pip install pyAesCrypt

# brute-force
python pyaescrypt_bf.py -w /usr/share/wordlists/rockyou.txt -f web_20250806_120723.zip.aes -o decrypted.zip
```