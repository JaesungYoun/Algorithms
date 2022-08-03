import sys
from itertools import permutations

N = int(sys.stdin.readline())

arr = []
check = [False] * N

def dfs(depth):
    if depth == N:
        print(*arr)
        return
    
    for i in range(N):
        if check[i] == True:
            continue
        arr.append(i+1)
        check[i] = True
        dfs(depth + 1)
        arr.pop()
        
        check[i] = False
        
dfs(0)
