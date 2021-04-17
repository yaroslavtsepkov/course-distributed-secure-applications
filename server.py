#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import io
import threading
from PIL import Image, ImageFilter
from tqdm import tqdm


if __name__ == '__main__':
    addr = socket.gethostname()
    port = 1235
    server = socket.socket()
    server.bind((addr,port))
    server.listen()
    conn, addr = server.accept()
    f = open('server_duck.png','wb')
    image_chunk = conn.recv(2048)

    while image_chunk:
        f.write(image_chunk)
        image_chunk = conn.recv(2048)

    f.close()
    conn.close()