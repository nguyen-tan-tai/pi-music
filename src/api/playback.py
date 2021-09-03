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
        if action == 'play':
            print(self.router.get_post_json_body())
        elif action == 'pause':
            print('pause')
            Player.get_instance().pause()
        elif action == 'resume':
            print('resume')
        elif action == 'next':
            print('next')
        self.router.ok_json('{"volume":' + current_volume + '}')
