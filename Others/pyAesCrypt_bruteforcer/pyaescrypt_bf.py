import pyAesCrypt
import argparse
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('-w', '--wordlist', required=True, help='Cracking wordlist')
parser.add_argument('-f', '--file', required=True, help='File to decryp')
parser.add_argument('-o', '--output', default='output.zip', help='Output file name')
args = parser.parse_args()

with open(args.wordlist, 'r', errors = 'ignore') as f: wordlist = f.readlines()

input_file = args.file
output_file = args.output

buffer_size = 64 * 1024  # 64KB

wl_len = len(wordlist)
i = 1
for password in wordlist:
    password = password.strip()
    try: 
        pyAesCrypt.decryptFile(input_file, output_file, password, buffer_size)
        print(f"\nPassword found: {password}")
        sys.exit(0)
    except Exception:
        if os.path.exists(output_file):
            os.remove(output_file)
    print(f"[{i}/{wl_len}] - Password not found yet", end="\r")
    i += 1

