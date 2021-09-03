import simplejson
from urllib.parse import urlparse
from urllib.parse import parse_qs
from pprint import pprint
from player import Player


class Playback:
    router = None

    def __init__(self, router):
        self.router = router

    def handle(self):
        command = self.router.path.strip("/").split('/')
        action = command[1]
        if action == 'queue':
            option = command[2]
            if option == 'add':
                Player.add_to_queue(['nhac_tre/canh_buom_trong_mua-chu_thuy_quynh.mp3', 'nhac_tre/doi_anh_den_thi_hoa_cung_tan-phuong_phuong_thao.mp3', 'nhac_tre/tránh_duyên.mp3'])
            elif option == 'replace':
                Player.replace_queue(['nhac_gia/ok.mp3'])

        elif action == 'pause':
            Player.pause(command[2] == 'true')

        elif action == 'loop':
            Player.loop(command[2] == 'true')

        elif action == 'shuttle':
            Player.shuttle(command[2] == 'true')

        elif action == 'play':
            Player.play()

        elif action == 'prev':
            Player.prev()

        elif action == 'next':
            Player.next()

        self.router.ok_json(Player.status())
