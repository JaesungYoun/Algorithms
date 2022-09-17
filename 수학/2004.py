import sys
from itertools import combinations
n,m= map(int,sys.stdin.readline().split())

def five(n):
    cnt = 0
    while n != 0:
        print(cnt)
        print(n)
        n //= 5
        cnt += n
    return cnt

def two(n):
    cnt = 0
    while n != 0:
        n //= 2
        cnt += n 
    return cnt
print(five(125))

if m == 0:
    print(0)
else:
    print(min(two(n) - two(m) - two(n-m), five(n) - five(m) - five(n-m)))