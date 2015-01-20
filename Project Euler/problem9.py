#-*- coding: utf-8 -*-
'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''
import math

def check(b):
    i, a, result = 1, 0, 0
    b = math.pow(b, 2)
    
    while result <= 1000 and a < b:
        a = math.pow(i, 2)       
        c = a + b
        result = a + b + c
        
        if result == 1000:
            return [a, b, c]
            
        i = i + 1
        
    return None
    
b = 1
    
while True:
    result = check(b)
    if not result == None:
        print 'jee ' + str(result)
        #break
    
    b = b+1
    
    