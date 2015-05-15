# write.py

import os

def make_story1():
    if os.path.isfile('store.txt'):
        print('story.txt already exists')
    else:
        f = open('story.txt', 'w')
        f.write('Mary has a little lamb, \n')
        f.write(' and then she has some more.\n')
