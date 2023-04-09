import sys
from collections import defaultdict

N = int(sys.stdin.readline())

h = list(map(int,sys.stdin.readline().split()))

stack = []
result = [0 for _ in range(N)]

for i in range(N):
    while stack: 
        if stack[-1][1] >= h[i]: #왼쪽이 더 크다면 
            result[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    
    stack.append([i,h[i]])
    
print(*result)