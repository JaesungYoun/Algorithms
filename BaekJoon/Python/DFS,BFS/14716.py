import sys
sys.setrecursionlimit(100000)
M,N = map(int,sys.stdin.readline().split())

mat = []
for _ in range(M):
    mat.append(list(map(int,sys.stdin.readline().split())))


def dfs(x,y):
    if not (0<=x<M and 0<=y<N):
        return False
    
    if mat[x][y] == 1:
        mat[x][y] = 0
        
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y+1)
        dfs(x-1,y+1)
        dfs(x+1,y-1)
        dfs(x-1,y-1)
        return True
    return False

cnt = 0
for i in range(M):
    for j in range(N):
        if dfs(i,j):
            cnt += 1
        
print(cnt)     

