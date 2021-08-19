cd ~/pi-music

git fetch --prune
git reset --hard origin/dev

sudo rm -rf /var/www/html/*
sudo cp -rf ~/pi-music/www/* /var/www/html/

kill $(cat ./pidfile) 2> /dev/null

rm ./pidfile 2> /dev/null

python3 ~/pi-music/src/pimusic.py
