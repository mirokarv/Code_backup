'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

#we check that if number is dividable by prime numbers that are in a list
def checkPrime(x, list):
    for i in list:
        if x%i == 0:
            return False
    return True

def prime():
    #2 is a only even prime number, therefore i = 3
    i, list = 3, [2]
    
    while len(list) <= 10001:
        if checkPrime(i, list):
            list.append(i)
        i = i+2 #we only test odd numbers
            
    return list       
            
primeList = prime()
print primeList[-1]