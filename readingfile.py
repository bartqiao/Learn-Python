__author__ = 'Bart Qiao'

def print_file(fname):
    f = open(fname, 'r')
    for line in f:
        print(line, end = '')
    f.close()