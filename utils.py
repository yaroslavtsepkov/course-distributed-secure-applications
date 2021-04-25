import socket
from PIL import Image, ImageFilter
import random
import numpy as np

def clearImage(path: str):
    img = Image.open(path)
    img = img.filter(ImageFilter.MedianFilter(size=5))
    img.save('clear_duck.png','png')

def sendImage(client: socket, path: str):
    """ 
    this function to send message to server 
    :param client is socket
    :param path is relative path to image
    """
    f = open(path, mode='rb')
    image_chunk = f.read(2048)
    while image_chunk:
        client.send(image_chunk)
        image_chunk = f.read(2048)
    f.close()

def saveImage2File(conn: socket, path: str):
    """
    docs
    """
    f = open(path,'wb')
    image_chunk = conn.recv(2048)
    while image_chunk:
        f.write(image_chunk)
        image_chunk = conn.recv(2048)
    f.close()

def greaseImage(path: str, amount: float):
    # source https://quares.ru/?id=127705
    # отсюда была взята функция добавления шума
    img = Image.open(path)
    output = np.copy(np.array(img))

    # add salt
    nb_salt = np.ceil(amount * output.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(nb_salt)) for i in output.shape]
    output[coords] = 1

    # add pepper
    nb_pepper = np.ceil(amount* output.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(nb_pepper)) for i in output.shape]
    output[coords] = 0
    img = Image.fromarray(output)
    img.save('noisy_duck.png') 