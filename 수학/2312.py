import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    i = 2
    cnt = 0 
    
    while 1:
        if N % i == 0:
            if N == i:
                cnt += 1
                N //= i
                print(i,cnt)
                break
            else:
                cnt += 1
                N //= i
        else:
            if cnt != 0 :
                print(i,cnt)
            i += 1
            cnt = 0
        
        
    
        