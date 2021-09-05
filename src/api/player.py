import dbus
import json
import os

class Dbus:

    @staticmethod
    def get_bus_object():
        try:
            with open('/tmp/omxplayerdbus.pi', 'r+') as fd:
                sock_info = fd.read().strip()
                bus = dbus.bus.BusConnection(sock_info)
                return bus.get_object('org.mpris.MediaPlayer2.omxplayer', '/org/mpris/MediaPlayer2', introspect=False)
        except Exception as e:
            return null

    @staticmethod
    def get_ifp():
        return dbus.Interface(Dbus.get_bus_object(), 'org.freedesktop.DBus.Properties')

    @staticmethod
    def get_ifk():
        return dbus.Interface(Dbus.get_bus_object(), 'org.mpris.MediaPlayer2.Player')

    @staticmethod
    def is_dbus_available():
        try:
            get_bus_object()
            return True
        except Exception as e:
            return False

    @staticmethod
    def get_duration():
        return Dbus.get_ifk().Duration()

    @staticmethod
    def pause():
        return Dbus.get_ifk().Pause()

    @staticmethod
    def play():
        return Dbus.get_ifk().Play()

    @staticmethod
    def get_source():
        return Dbus.get_ifk().GetSource()

    @staticmethod
    def open_uri(uri):
        return Dbus.get_ifk().OpenUri(uri)


class Player:
    __queue = []
    __index = 0
    __pause = False
    __shuttle = False
    __loop = False

    @staticmethod
    def add_to_queue(list):
        Player.__queue.extend(list)

    @staticmethod
    def replace_queue(list):
        Player.__queue = list
        Player.__index = 0
        Player.play()

    @staticmethod
    def play():
        if Player.__index >= len(Player.__queue):
            Player.__index = len(Player.__queue) - 1

        Player.pause(False)

        if Dbus.is_dbus_available():
            Dbus.open_uri('~/mp3/' + Player.__queue[Player.__index])
        else:
            os.system('omxplayer -o alsa:hw:1,0 ~/mp3/' + Player.__queue[Player.__index] + ' > /dev/null 2>&1&')


    @staticmethod
    def pause(isPause):
        if Dbus.is_dbus_available():
            if isPause:
                Dbus.pause();
            else:
                Dbus.play();
        Player.__pause = isPause

    @staticmethod
    def loop(isLoop):
        Player.__loop = isLoop

    @staticmethod
    def shuttle(isShuttle):
        Player.__shuttle = isShuttle

    @staticmethod
    def prev():
        if Player.__index > 0:
            Player.__index = Player.__index - 1
        else:
            if Player.__loop:
                Player.__index = len(Player.__queue) - 1

        Player.play()

    @staticmethod
    def next():
        if Player.__index < len(Player.__queue) - 1:
            Player.__index = Player.__index + 1
        else:
            if Player.__loop:
                Player.__index = 0

        Player.play()

    @staticmethod
    def status():
        x = {
            "queue": Player.__queue,
            "index": Player.__index,
            "play": Dbus.is_dbus_available(),
            "pause": Player.__pause,
            "shuttle": Player.__shuttle,
            "loop": Player.__loop
        }
        return json.dumps(x);
