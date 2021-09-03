import socket
import http.server
import simplejson
from urllib.parse import urlparse
from urllib.parse import parse_qs
from pprint import pprint

from playback import Playback
from volume import Volume
from media import Media


class Router(http.server.SimpleHTTPRequestHandler):

    def handle_one_request(self):
        try:
            self.raw_requestline = self.rfile.readline(65537)
            if len(self.raw_requestline) > 65536:
                self.requestline = ''
                self.request_version = ''
                self.command = ''
                self.send_error(HTTPStatus.REQUEST_URI_TOO_LONG)
                return
            if not self.raw_requestline:
                self.close_connection = True
                return
            if not self.parse_request():
                # An error code has been sent, just exit
                return
            mname = 'do_route'
            if not hasattr(self, mname):
                self.send_error(
                    HTTPStatus.NOT_IMPLEMENTED,
                    "Unsupported method (%r)" % self.command)
                return
            method = getattr(self, mname)
            method()
            self.wfile.flush()  # actually send the response if not already done.
        except socket.timeout as e:
            # a read or a write timed out.  Discard this connection
            self.log_error("Request timed out: %r", e)
            self.close_connection = True
            return

    def do_route(self):
        # try:
            controller = self.path.strip("/").split('/')[0].capitalize()
            klass = globals()[controller]
            handler = klass(self)
            handler.handle()
        # except Exception as e:
        #     print(e)
        #     self.send_response(500)

    def ok_html(self, html):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(json))
        self.end_headers()
        self.wfile.write(json.encode("utf-8"))

    def ok_json(self, json):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Content-length", len(json))
        self.end_headers()
        self.wfile.write(json.encode("utf-8"))

    def get_post_json_body(self):
        post_body = self.rfile.read(int(self.headers['content-length']))
        return simplejson.loads(post_body)
