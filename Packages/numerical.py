def isPrime(n):
    flag =1
    if n==2:
        return True
    for i in range (2,n//2+1):
        if n%i==0:
            return False
            flag=0
    if flag ==1:
        return True

def numberofPrimeFactors(n):
    count=0
    if isPrime(n):
        return 1
    for i in range (2,n//2+1):
            if isPrime(i) and n%i==0:
               count+=1
    return count