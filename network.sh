#Check connectivity
#If connectivity fails restart networking interface

if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; then
  echo "IPv4 is up"
else
  echo "IPv4 is down"
  sudo /etc/init.d/networking restart
fi
