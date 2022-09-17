import sys

import math

def isPrime(x): 
    if x == 1:
        return False
    
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

N = int(sys.stdin.readline())
res = 0 

for i in range(N,1000001):
    
    if str(i) == str(i)[::-1]:
        if isPrime(i):
            res = i
            break
if res == 0:
    res = 1003001

print(res)