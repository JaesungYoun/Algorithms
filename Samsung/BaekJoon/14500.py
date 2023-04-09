N,M = map(int,input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))

result = 0
max_val = max(map(max, mat))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(depth,total,x,y):
    global max_val,result
    
    if total + max_val *(3-depth) <= result:
        return
    if depth == 3:
        result = max(result,total)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
            if depth == 1:
                visited[nx][ny] = 1
                dfs(depth + 1, total + mat[nx][ny],x,y) # 뻐큐모양 
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(depth + 1, total + mat[nx][ny],nx,ny)
            visited[nx][ny] = 0
            


visited = [[0] * M for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(N):
    for j in range(M):
        visited[i][j] = 1 # 한 칸마다 탐색 
        dfs(0,mat[i][j],i,j)
        visited[i][j] = 0 

print(result)