'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

def checkPrime(x, list):
    for i in list:
        if x%i == 0 or x/2 > i:
            return False
    return True

def prime():
    #2 is a only even prime number, therefore i = 3
    i, list = 3, [2]
    
    while i <= 2000000:
        if checkPrime(i, list):
            list.append(i)
            print i
        i = i+2 #we only test odd numbers
            
    return list       
            
primeList = prime()
total = 0

for i in primeList:
    total = total + i
    
#142913828922
print total