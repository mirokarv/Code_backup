'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import time

def check(i, list):
    print 'test num: ' + str(i)
    for j in list:
        if i%j == 0:
            return False
            
    return True
    
    
x = 13195
x = 600851475143

def algo(x):
    list = []
    i = 3
    y = x/i
    print 'y on: ' + str(y)

    t1 = time.time()

    while i < y:
        if x%i == 0:
            if check(i, list):
                list.append(i)
            y = x/i
        i = i + 2

    t2 = time.time()
    t = t2 - t1
    print t
    print list
    print 'largest prime: ' + str(list[-1])

   
algo(x)
  
'''    
x = 600851475143
x = 1319512 #0.243999958038
list = []
i = 2
#for i in xrange(2,x-1):

t1 = time.time()

while i < x:
    if x%i == 0:
        if not list == []:
            if check(i, list) == True:
                list.append(i)
        else:
            list.append(i)
    i= i*i +1
    
t2 = time.time()
print list
t = t2 - t1
print t
'''    