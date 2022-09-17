import sys
sys.setrecursionlimit(100000)

N,M,K = map(int,sys.stdin.readline().split())

mat = []
visited = [[0] * (M+1) for _ in range(N+1)]
for _ in range(K):
    r,c = map(int,sys.stdin.readline().split())
    visited[r][c] = 1

def dfs(x,y):
    global area 
    if not (1<=x<N+1 and 1<=y<M+1):
        return False
    
    if visited[x][y] == 1:
        visited[x][y] = 0
        area += 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False        
        

max_area = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        area = 0 
        if dfs(i,j) == True:
            max_area = max(max_area,area)
        
print(max_area)
