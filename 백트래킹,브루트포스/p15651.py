import sys

N,M = map(int,sys.stdin.readline().split())



arr = []

check_list = [False] * N

def dfs(depth):
    if depth == M:
        print(*arr)
        return

    for i in range(0,N):
        if check_list[i] == True:
            continue
        
        arr.append(i+1)
        dfs(depth + 1)
        check_list[i] = True
        arr.pop()
        
        for j in range(0,i):
            check_list[i] = False
        

dfs(0)