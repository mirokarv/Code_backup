#-*- coding: utf-8 -*-

import sys, os

#writing stuff to the file 
def writer(text, argv):
    #gets the file path
    codeDirectory = argv[1]
    codeDirectory = codeDirectory[:codeDirectory.rfind('\\')]
    filename = argv[2] + '.txt'
    #creating a file if needed and accessing to it
    file = os.path.join(codeDirectory, filename) 
    f = open (file, 'a')
    input = text.encode("utf8") + '\n'

    f.write(input)
    f.close()
    