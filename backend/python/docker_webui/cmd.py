#!/usr/bin/env python

import time
import traceback
import argparse

from docker_webui.app import app

def parse_args():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--host', type=str, dest='host', default='127.0.0.1',
        help="The host address of the backend server. Default: 127.0.0.1")
    argparser.add_argument('-p', '--port', type=str, dest='port', default='8080',
        help="The port of the backend server. Default: 8080")
    return argparser.parse_args()

def main():
    args = parse_args()
    app.run(host=args.host, port=args.port)


if __name__ == '__main__':
    main()
