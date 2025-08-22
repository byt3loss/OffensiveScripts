from rawhttpy import RawHTTPy
import requests as req
import argparse
import sys
import string

parser = argparse.ArgumentParser()
parser.add_argument("-rf", "--request-file", help="File containing raw HTTP request")
parser.add_argument("-w", "--wordlist", help="Fuzzing wordlist")
parser.add_argument("-to", "--timeout", help="Waiting after sending each request", type=int, default=5)
parser.add_argument("-wfs", "--wordlist-filer-start", help="Exclude words starting with the specified character(s). Args must be separated by spaces.", nargs="+")
parser.add_argument("-wfsp", "--wordlist-filer-start-punctuation", help="Exclude words starting with punctuation.", action="store_true")
args = parser.parse_args()

if not args.request_file or not args.wordlist:
    print("Error: -rf and -w flags are mandatory.")
    sys.exit(1)

def filter_wl(wl):
    filtered_list = wl
    if args.wordlist_filer_start:
        for ch in args.wordlist_filer_start:
            filtered_list = list(filter(lambda x: not x.startswith(ch), filtered_list))
    if args.wordlist_filer_start_punctuation:
        for ch in string.punctuation:
            filtered_list = list(filter(lambda x: not x.startswith(ch), filtered_list))
    return filtered_list

sym = "[+]"

# request
with open(args.request_file, "r") as f: httpy = RawHTTPy(f.read(), ssl=False)

# wordlist (e.g. /usr/share/wordlists/amass/subdomains-top1mil-5000.txt)
with open(args.wordlist, "r") as f: wl = f.readlines()

print(f"{sym} Loaded request to URL: {httpy.url}")
print(f"{sym} Body found: {httpy.body}")
print(f"{sym} FUZZING started on the target")

wl = filter_wl(wl)
wl_length = len(wl)
index = 0

#timeout = args.timeout or 10

for w in wl:
    index +=1
    subdomain = w.strip()
    data = {}
    print(f"{sym} [{index}/{wl_length}] - {subdomain}" + " "*20, end="\r")
    for k,v in httpy.body.items():
        data[k] = v.replace('FUZZME', subdomain)
    try:
        res = req.post(httpy.url, headers=httpy.headers, data=data, timeout=args.timeout)
        if res.text:
            print(f"\n{sym} Valid subdomain found: {subdomain}")
    except TimeoutError:
        continue
    except req.exceptions.ReadTimeout:
        continue
    except Exception as e:
        print(e)
    
