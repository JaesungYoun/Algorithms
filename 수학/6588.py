import sys

check = [True] * 1000001
primes = []

    
for i in range(2,1000001):
    if check[i]:
        primes.append(i)
        for j in range(2*i,1000001,i):
            check[j] = False
    

while 1: 
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(3,1000001,2):
        if check[i] == True:
            if check[n-i] == True:
                print("%d = %d + %d"%(n , i , n-i))
                break
    else:
        print("Goldbach's conjecture is wrong.")