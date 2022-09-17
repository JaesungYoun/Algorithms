import sys
from itertools import combinations

N = int(sys.stdin.readline())

flavor = []

for _ in range(N):
    flavor.append(list(map(int,sys.stdin.readline().strip().split())))
 
c = []
for i in range(1,N+1):
    c.append(combinations(flavor,i))
result = sys.maxsize

for i in c:
    for j in i:
        s_taste,b_taste = 1,0
        for s,b in j:
            s_taste *= s
            b_taste += b
        result = min(result,abs(s_taste - b_taste))
print(result)
