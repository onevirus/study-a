url=('https://ident.me' 'https://api.ipify.org')

for u in ${url[@]}; do
  curl -6 -s -m 2 $u
done

echo "---"

for u in ${url[@]}; do
  curl -4 -s -m 2 $u && break
done
