# Python Werkzeug

## PIN Generation Exploit

Werkzeug’s debug PIN is a pseudo-random 9-digit number that acts as a weak authentication mechanism when running a Flask app in debug mode. It's generated using system-specific identifiers:

- Machine-ID (/etc/machine-id or /proc/sys/kernel/random/boot_id)
    - A unique identifier for the system.
- MAC Address (/sys/class/net/eth0/address)
    - The network interface's MAC address, converted to an integer.
- Cgroup (/proc/self/cgroup) (in some cases)
    - Used in some containerized environments to generate a more unique fingerprint.

If an attacker gains access to these files on the server, they can generate the Werkzeug PIN and achieve RCE via the `/console` endpoint.