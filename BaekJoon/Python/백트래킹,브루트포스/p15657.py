import sys

N,M = map(int,sys.stdin.readline().split())

numbers = list(map(int,sys.stdin.readline().split()))
numbers.sort()
arr = []
check = [False] * N

def dfs(depth):
    if depth == M:
        print(*arr)
        return

    for i in range(len(numbers)):
        if check[i] == True:
            continue
        
        arr.append(numbers[i])
        dfs(depth + 1)
        check[i] = True
        arr.pop()
        
        for j in range(i+1,len(numbers)):
            check[j] = False
    
dfs(0)        
                