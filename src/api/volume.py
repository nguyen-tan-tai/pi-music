import os
import simplejson
from urllib.parse import urlparse
from urllib.parse import parse_qs
from pprint import pprint


class Volume:
    router = None

    def __init__(self, router):
        self.router = router

    def handle(self):
        command = self.router.path.strip("/").split('/')
        action = command[1]
        value = command[2]
        if action == 'set':
            os.system('amixer -c 1 set Speaker ' + value + '%')

        elif action == 'up':
            os.system('amixer -c 1 set Speaker ' + value + '%+')

        elif action == 'down':
            os.system('amixer -c 1 set Speaker ' + value + '%-')

        current_volume = os.popen('amixer -c 1 get Speaker | grep -Po -m 1 "[0-9]{2,3}%" | sed -e "s/%//g"').read();

        self.router.ok_json('{"volume":' + current_volume + '}')
