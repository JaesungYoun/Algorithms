import sys
sys.setrecursionlimit(1000000)
R,C = map(int,sys.stdin.readline().split())


mat = []

for i in range(R):
    mat.append(list(map(str,sys.stdin.readline())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0] * C for _ in range(R)]



def dfs(x,y):
    global s,w
    visited[x][y] = 1
    
    if mat[x][y] == 'v':
        w += 1
    elif mat[x][y] == 'k':
        s += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
               
        if 0<=nx<R and 0<=ny<C:
            if visited[nx][ny] == 0 and mat[nx][ny] != '#':
                dfs(nx,ny)
            
    
sheep = 0
wolf = 0
for i in range(R):
    for j in range(C):
        if visited[i][j] == 0:
            s = 0
            w = 0 
            dfs(i,j)
            if s > w:
                w = 0
            else:
                s = 0
            sheep += s
            wolf += w
            

print(sheep,wolf)