__author__ = 'Bart Qiao'

import os

def list_cwd():
    return os.listdir(os.getcwd())

def files_cwd():
    return [p for p in list_cwd() if os.path.isfile(p)]

def folders_cwd():
    return [p for p in list_cwd() if os.path.isdir(p)]

def list_py(path, extension):
    if path == None:
        path = os.getcwd()
        print('Current folder is: ', path)
        return [fname for fname in os.listdir(path) if os.path.isfile(fname) if fname.endswith(extension)]

def size_in_bytes(fname):
    return os.stat(fname).st_size

def cwd_size_in_bytes():
    total  = 0
    for name in files_cwd():
        file_size = size_in_bytes(name)
        total = total + file_size
        print('File name is: ' + name, '| File size is: ' + str(file_size))
    return total

def print_file(fname):
    print(open(fname, 'r').read())

def cwd_print_file():
    for name in list_py():
        print()
        print('*************************')
        print('File name is: ', name)
        print('=========================')
        print_file(name)
        print()

def write_file():
    if os.path.isfile('story.txt'):
        print('story.txt already exists.')
    else:
        f = open('story.txt',  'w')
        f.write('Mary has a little lamb, \n')
        f.write('and then she has some more. \n')

def add_to_story(line, fname):
    f = open(fname, 'a')
    f.write(line)

def insert_title(title, fname):
    f = open(fname, 'r+')
    temp = f.read()
    temp = title + '\n\n' + temp
    f.seek(0) # reset file pointer to beginning
    f.write(temp)

def is_gif(extension):
    file = list_py(None, extension)
    print('File name is:', file[0])
    fname = file[0]
    f = open(fname, 'br')
    first4 = tuple(f.read(4))
    #print('First 4 characters of file ' + fname + ' is ', first4)
    if first4 == (0x47, 0x49, 0x46, 0x38):
        print('The file "' + fname + '" is a gif file.')
    else:
        print('not gif file')
            #if first4 == (0x47, 0x49, 0x46, 0x38)

#print(list_py(None, '.gif'))
#print('------------------------------------\n' + 'Total size of the files is: ', cwd_size_in_bytes())
#print('\n------------------------------------')
#print("Now we will print the files' content", cwd_print_file())
#write_file()
#add_to_story('how are you doing? \n', 'story.txt')
#insert_title('who are you?', 'story.txt')
is_gif('.gif')