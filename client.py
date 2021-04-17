#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import io
from PIL import Image
from tqdm import tqdm

if __name__ == '__main__':
    client = socket.socket()
    addr = socket.gethostname()
    port = 1235
    client.connect((addr, port))
    f = open('duck.png','rb')
    image_chunk = f.read(2048)

    while image_chunk:
        client.send(image_chunk)
        image_chunk = f.read(2048)

    f.close()
    client.close()