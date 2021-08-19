import dbus, time


class Player:


    def get_omx_player_bus(self):
        with open('/tmp/omxplayerdbus.pi', 'r+') as fd:
            sock_info = fd.read().strip()

        bus = dbus.bus.BusConnection(sock_info)

        obj = bus.get_object('org.mpris.MediaPlayer2.omxplayer', '/org/mpris/MediaPlayer2', introspect=False)
        return dbus.Interface(obj, 'org.mpris.MediaPlayer2.Player')


    def play(self, list):
        print(list)
