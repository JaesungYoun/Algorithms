import sys

N,M = map(int,sys.stdin.readline().split())

mat = []
for _ in range(N):
    mat.append(list(map(int,sys.stdin.readline().split())))

    
result = 0
max_val = max(map(max, mat))
def dfs(depth,total,x,y):
    global max_val,result
    
    if total + max_val *(4-depth) <= result:
        return
    if depth == 4:
        result = max(result,total)
        return
    
    for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if depth == 2:
                    visited[nx][ny] = 1
                    dfs(depth + 1, total + mat[nx][ny],x,y)
                    visited[nx][ny] = 0
                visited[nx][ny] = 1
                dfs(depth + 1, total + mat[nx][ny],nx,ny)
                visited[nx][ny] = 0
                
visited = [[0] * M for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(0,0,i,j)
        visited[i][j] = 0 

print(result)