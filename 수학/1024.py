import sys

N,L = map(int,sys.stdin.readline().split())


for i in range(L,101):
    x = N - (i * (i-1) / 2)
    
    if x % i == 0:
        x = x // i
        
        if x >= 0:
            for j in range(i):
                print(int(x+j),end = ' ')
            
            break

else:
    print(-1)