#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from utils import saveImage2File, clearImage

def run():
    addr, port = socket.gethostname(), 12356
    server = socket.socket()
    server.bind((addr, port))
    server.listen()
    conn, addr = server.accept()
    saveImage2File(conn, 'raw_duck.png')
    clearImage('raw_duck.png')
    conn.close()


if __name__ == '__main__':
    run()