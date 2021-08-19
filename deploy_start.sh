cd ~/pi-music

git fetch --prune
git reset --hard origin/dev

sudo rm -rf /var/www/html/*
sudo cp -rf ~/pi-music/www/* /var/www/html/

if [[ -f ~/pi-music/pidfile ]] ; then
    kill $(cat ~/pi-music/pidfile) 2> /dev/null
    rm ~/pi-music/pidfile 2> /dev/null
fi

python3 ~/pi-music/src/pimusic.py
