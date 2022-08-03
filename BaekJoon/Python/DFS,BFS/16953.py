import sys

A,B = map(int,sys.stdin.readline().split())
cnt = 1
while 1:
    if A == B:
        break
    elif A > B or (B % 10 != 1 and B % 2 != 0):
        cnt = -1
        break
    elif B % 10 == 1:
        B //= 10
        cnt += 1
    elif B % 2 ==0:
        B //= 2
        cnt += 1
        
    
    
print(cnt)
