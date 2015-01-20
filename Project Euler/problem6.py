#-*- coding: utf-8 -*-
'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. 
'''
import math

testNum = 100

def sumOfSquareOfNaturalNumbers(x):
    i, total = 1, 0
    while i <= x:
        total = total + math.pow(i, 2)
        i = i+1
        
    return total
    
def squareOfNaturalNumbers(x):
    i, total = 1, 0
    while i <= x:
        total = total + i
        i = i+1
        
    return math.pow(total, 2) 
    
x = sumOfSquareOfNaturalNumbers(testNum)
y = squareOfNaturalNumbers(testNum)
print str(y) + ' - ' + str(x)+ ' = ' + str(y - x)