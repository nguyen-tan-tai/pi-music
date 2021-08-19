#!/bin/bash

cd ~/pi-music

git fetch --prune
git reset --hard origin/dev

sudo rm -rf /var/www/html/*
sudo cp -rf ~/pi-music/www/* /var/www/html/

if [[ -f ~/pi-music/pidfile ]] ; then
    kill $(cat ~/pi-music/pidfile)
    rm ~/pi-music/pidfile
fi

python3 ~/pi-music/src/pimusic.py
