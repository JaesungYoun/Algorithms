import sys
import math 
N = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))

B,C  = map(int,sys.stdin.readline().split())


cnt = 0
for i in A:
    i = i - B
    cnt += 1
    if i > 0:
        cnt += i//C
        if i % C != 0:
            cnt += 1
        
    
print(cnt)