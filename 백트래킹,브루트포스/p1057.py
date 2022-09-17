import sys

N,k,l = map(int,sys.stdin.readline().split())


count = 1
while 1:
    if abs(k-l) == 1 and min(k,l) % 2 == 1:
        break
    
    if k % 2 == 0:
        k = (k//2)
    elif k% 2 == 1:
        k = (k//2) + 1
    if l % 2 == 0:
        l = (l//2) 
    elif l% 2 == 1:
        l = (l//2) + 1
    
    count += 1
    
print(count)
    
    