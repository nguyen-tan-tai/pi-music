# pi-music

## Setup pi
- Install Raspberry Pi OS using Raspberry Pi Imager -> https://www.raspberrypi.org/software/
- https://www.raspberrypi.org/software/operating-systems/

https://desertbot.io/blog/setup-pi-zero-w-headless-wifi

Create ssh file in boot drive

```
touch /e/ssh
```

Create wpa_supplicant.conf file in boot drive

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=VI

network={
     ssid="your_wifi_ssid"
     psk="your_wifi_pwd"
     scan_ssid=1
}
```


```
$ sudo apt install omxplayer

```

wget https://github.com/popcornmix/omxplayer/blob/master/dbuscontrol.sh

update 
OMXPLAYER_DBUS_ADDR="/tmp/omxplayerdbus.${USER:-root}"
OMXPLAYER_DBUS_PID="/tmp/omxplayerdbus.${USER:-root}.pid"

OMXPLAYER_DBUS_ADDR="/tmp/omxplayerdbus.${USER}"
OMXPLAYER_DBUS_PID="/tmp/omxplayerdbus.${USER}.pid"

https://github.com/ytdl-org/youtube-dl

sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl

sudo apt-get install ffmpeg


https://pimylifeup.com/raspberry-pi-ufw/