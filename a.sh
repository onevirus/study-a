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
