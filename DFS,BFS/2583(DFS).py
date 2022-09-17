import sys
sys.setrecursionlimit(10000)
M,N,K = map(int,sys.stdin.readline().split())

visited = [[0] * M for _ in range(N)]

for _ in range(K):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            visited[i][j] = 1    
    
def dfs(x,y):
    global area
    if not (0 <= x < N and 0 <= y < M):
        return False
    
    if visited[x][y] == 0:
       
        visited[x][y] = 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)    
        area += 1
        return True
    return False


areas = []
cnt = 0
for i in range(N):
    for j in range(M):
        area = 0 
        if dfs(i,j) == True:
            cnt += 1
            areas.append(area)
areas.sort()
print(cnt)
print(*areas)
