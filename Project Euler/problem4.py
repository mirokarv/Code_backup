suurin = None
    
def palid(num):
    i = 0
    num = str(num)
    lenght = len(num)
    reverseNum = ""
    while i < lenght:
        reverseNum = reverseNum + num[lenght -i-1]
        
        i = i+1
        
    if reverseNum == num:
        print 'truuu ' + num
        return True
        
    return False

def check(num):
    global suurin
    if num > suurin:
        suurin = num
        
def calcu(x, y): 
    global suurin
    
    while 0 < x:
        sum = x * y
        
        if suurin > sum:
            return False
            
        if palid(sum):
            check(sum)
            return True
            
        x = x -1
        
    return False
        
def main():
    x, y = 999, 999
    i = y/2
    while i < y:
        calcu(x, y)
        y = y -1
    
    print 'suurin: ' + str(suurin)
    
main()