#-*- coding: utf-8 -*-

import os.path, sys
from writer import writer

#function checks given arguments
def argument(argv):
    #number of required arguments is 3
    if not len(argv) == 3:
        print u'annappa koodifilun polku käynnistys argumentiksi ja tietoston nimi minne tallennetaan tulokset'
        sys.exit(1)
        
    #checks if first user given argument, file path is correct     
    if not os.path.isfile(argv[1]):
        print u'filua ei löytynyt. käynistä ohjelma muodossa: ' + 'C:\loc laskuri.py "C:\\folder\script.py" "tiedosto nimi"'
        sys.exit(1)
        

def counter():
   
    def __init__(self, content, methodList):
        self.content = content #stores the file content
        self.methodList = methodList #stored the method names, loc and logical lines
        
    #min and max (int) defines the lines in file which are counted
    def locCounter(min, max):
        #initializing variables
        lines, logicalLines = 0, 0
        #runs all the lines in content between range min to max
        for line in counter.content[min:max]:
            #encoding the each line to utf-8, so other function calls can understand all chars
            line = unicode(line, "utf-8")
            
            #checks if line contains characters, tabs and whitespaces are ignored
            if any(c.isalpha() for c in line):
                #checks if there is code before the comment
                line = line.split(u'#',1)[0]
                if any(c.isalpha() for c in line):
                    logicalLines = logicalLines +1
                    lines = lines +1
                        
                #if only comment is found    
                else:
                    lines = lines +1
        
        return [lines, logicalLines] 
        
         
    def blockCounter(): 
        blocks = 0 
        #self defined blocks and methods definitions
        listOfBlocks = [u'if', u'elif', u'else', u'for', u'while', u'with', u'try', u'except', u'def', u'class']
    
        for index, line in enumerate(counter.content):
            line = unicode(line, "utf-8")
            #takes list values one at the time
            for i in listOfBlocks:
                #checks if value defined in list is found in line
                if i + ' ' in line:
                    blocks = blocks +1
                    
                    #checks if it is a method
                    if i == 'def' or i == 'class':
                        #takes method name
                        methodName = line.split(i,1)[1]
                        
                        #checks in how deep block is
                        spaces, i = 0, 1
                        
                        #counting the deepness 
                        baseLine = counter.content[index].split('(',1)[0]

                        if any(c.isalpha() for c in baseLine):
                            spaces = baseLine.count(' ')
                            
                        #checks when method or block ends or new begins   
                        while True:
                            try:
                                if any(c.isalpha() for c in counter.content[index +i]):
                                    lineOfSpaces = counter.content[index +i].split('def',1)[0]
                                    if lineOfSpaces.count(' ') > spaces:
                                        i = i+1
                                        
                                    else:
                                        break
                                        
                                else:
                                    i = i+1
                            except:
                                break
                           
                        #counting loc for methods
                        methodLines = locCounter(index, index + i)
                        
                        #saving data to counter object
                        counter.methodList.append([methodName.split('(',1)[0], methodLines[1] -1, spaces/4, methodLines[0] -1])
                    
                    #if several blocks are found on same line, rest of them are ignored
                    break
                    
        return blocks

        
    def parser():
        for index, line in enumerate(counter.methodList):
            try:
                #0 = name, 1 = logical lines, 2 = deepness, 3 = loc 
                if line[2] < counter.methodList[index +1][2]:
                    for j in counter.methodList[index +1:]:
                        if j[2] > line[2]:
                            #reducing methods from objects, so we can get own loc for each method and object
                            line[1] = line[1] - j[1]
                            line[3] = line[3] - j[3]    
                            
                        else:
                            break
            except:
                pass
              
    
    def mean(index):
        #counting mean for objects methods
        mean, methods = 0, 0
        try:
            for line in counter.methodList[index +1:]:
                if not line[2] == 0:
                    mean = mean + line[1]
                    methods = methods +1
                    
            if not mean == 0:    
                return mean/methods
        except:
            pass
            
        return 0

    #script starts executing
       
    #checking arguments 
    argument(sys.argv)

    #opens the file 
    #because with is used, we don't have to close file separately 
    with open(sys.argv[1]) as f:
        content = f.readlines()
    
    counter.content = content
    counter.methodList = [] 
        
    #runs the loc counter 
    loc = locCounter(0, -1)
    #runs block counter
    blocks = blockCounter()
    
    #cleaning the method list and calculating mean
    parser()                
   
    #printing the results to the command prompt 
    result = '\nLOC: ' + str(loc[0]) + '\nBlocks: ' + str(blocks)  +'\nlookiset rivit: ' + str(loc[1])
    print result
    writer(result, sys.argv)
    print '\n\n'
    
    #prints methods and loc
    for index, i in enumerate(counter.methodList):
        result = '\n'
        if i[2] == 0:
            result = result + 'Object '
        else:
            result = result + 'Method '

        result = result + 'Nimi: ' + str(i[0]) + u' |  Lookisten rivien määrä: ' + str(i[1]) + u' | LOC: ' + str(i[3])
        
        if 'Object' in result:
            meann = mean(index)
            result = result + ' Mean: ' +str(meann)
        
        #writing results to the file
        writer(result, sys.argv)

        
#runs whole script  
counter()
