from os.path import isfile
import sys
import os
from PIL import Image


def converter(start, end):
    if (os.path.exists(start) == False):
        print('The starting dir doesn\'t exist')
        return
    if (os.path.exists(end) == False):
        os.makedirs(f'./{end}')
    images = os.listdir(start)
    if (len(images) < 1):
        print('There aren\'t any images at the start dir')
        return
    for i in images:
        img = Image.open(f'./{start}/{i}')
        img.save(f'./{end}/{i}', 'png')


if (len(sys.argv) == 3):
    start_dir = sys.argv[1]
    final_dir = sys.argv[2]
    converter(start_dir, final_dir)
else:
    print('A starting and ending location need to be supplied.')
