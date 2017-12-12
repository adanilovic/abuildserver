#!/usr/bin/env python

from sys import argv
from http.server import HTTPServer, BaseHTTPRequestHandler

class Build_Server(BaseHTTPRequestHandler):
    def do_POST(self):
        print("Hello Github Post World!")
        self.send_response(200)

def main(port=8080):

    webdir = '.'
    srvaddr = ('', port)
    srvobj = HTTPServer(srvaddr, Build_Server)
    srvobj.serve_forever()

if __name__ == '__main__':
    if len(argv) == 2:
        main(port=int(argv[1]))
    else:
        main()
