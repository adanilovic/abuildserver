#!/usr/bin/env python

from http.server import HTTPServer, CGIHTTPRequestHandler

def main():

    webdir = '.'
    port = 80
    srvaddr = ('', port)
    srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
    srvobj.serve_forever()

if __name__ == '__main__':
    main()
