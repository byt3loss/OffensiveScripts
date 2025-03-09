mac=$1
echo "02:56:c9:80:55:df" > /tmp/mac
hex_mac=$(sed 's/://g' /tmp/mac)
dec_mac=$(printf "%d" 0x$hex_mac)
echo $dec_mac
