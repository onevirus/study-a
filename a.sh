[ -f /proc/net/if_inet6 ] && echo 'IPv6 ready system!' || echo 'No IPv6 support found! Compile the kernel!!'

lsmod | grep -qw ipv6 && echo "IPv6 kernel driver loaded and configured." || echo "IPv6 not configured and/or driver loaded on the system."


curl -vv --ipv6 "[2607:f8b0:4002:c03::93]:80"

url=('https://ident.me' 'https://api.ipify.org')

ifconfig -a

for u in ${url[@]}; do
  curl -6 -s -m 2 $u
done

echo "---"

for u in ${url[@]}; do
  curl -4 -s -m 2 $u && break
done
