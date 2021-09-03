# import dbus, time
import json
import os


class Player:
    __queue = []
    __index = 0
    __play = False
    __pause = False
    __shuttle = False
    __loop = False

    @staticmethod
    def get_omx_player_bus():
        print(1)
        # with open('/tmp/omxplayerdbus.pi', 'r+') as fd:
        #     sock_info = fd.read().strip()
        #
        # bus = dbus.bus.BusConnection(sock_info)
        #
        # obj = bus.get_object('org.mpris.MediaPlayer2.omxplayer', '/org/mpris/MediaPlayer2', introspect=False)
        # return dbus.Interface(obj, 'org.mpris.MediaPlayer2.Player')

    @staticmethod
    def add_to_queue(list):
        Player.__queue.extend(list)

    def replace_queue(list):
        Player.__queue = list
        Player.__index = 0

    @staticmethod
    def play():
        if Player.__index < len(Player.__queue):
            __play = True
            os.system ('omxplayer -o alsa:hw:1,0 ~/mp3/' + Player.__queue[Player.__index])
            __play = False
        else:
            __play = False

    @staticmethod
    def pause(isPause):
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
            "play": Player.__play,
            "pause": Player.__pause,
            "shuttle": Player.__shuttle,
            "loop": Player.__loop
        }
        return json.dumps(x);
