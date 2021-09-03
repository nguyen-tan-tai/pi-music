# import dbus, time


class Player:
    __instance = None

    @staticmethod
    def get_instance():
        if Player.__instance == None:
            Player()
        return Player.__instance

    def __init__(self):
        if Player.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Player.__instance = self

    media_list = ["hoge", "fuga"]
    current_index = 0

    def get_omx_player_bus(self):
        print(1)
        # with open('/tmp/omxplayerdbus.pi', 'r+') as fd:
        #     sock_info = fd.read().strip()
        #
        # bus = dbus.bus.BusConnection(sock_info)
        #
        # obj = bus.get_object('org.mpris.MediaPlayer2.omxplayer', '/org/mpris/MediaPlayer2', introspect=False)
        # return dbus.Interface(obj, 'org.mpris.MediaPlayer2.Player')

    def play(self, list):
        print(list)

    def pause(self):
        print('pause')

    def resume(self):
        print('resume')

    def play_youtube(self, target):
        print('play_youtube' + target)

