import os
import simplejson
from urllib.parse import urlparse
from urllib.parse import parse_qs
from pprint import pprint


class Media:
    router = None

    def __init__(self, router):
        self.router = router

    def handle(self):
        command = self.router.path.strip("/").split('/')
        action = command[1]
        value = command[2]
        if action == 'list':
            self.router.ok_json('["~/mp3/nhac_tre/hoge.mp3", "~/mp3/nhac_tre/fuga.mp3"]')
        elif action == 'category':
            self.router.ok_json('["~/mp3/khong_loi", "~/mp3/nhac_tre/"]')
