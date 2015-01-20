'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

x = 20
i = x

def check(y, x): 
    #range runs through numbers between 2...x
    for i in range(2, x+1):
        if y%i != 0:
            return False
      
    return True

    
while True:
    #trying to find first number that can be divided by 2...x numbers
    if check(i, x):
        result = i
        break #stops that infinite loop when it has found it's target number
        
    i = i + x
    
print 'answer: ' + str(result)