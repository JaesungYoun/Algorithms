from collections import deque
N = int(input())
mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y,size):
    visited = [[0] * N for _ in range(N)]
    dist = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    eat = []
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                if mat[nx][ny] <= size:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
                    if mat[nx][ny] < size and mat[nx][ny] != 0:
                        eat.append((nx,ny,dist[nx][ny]))
 
    eat = sorted(eat,key = lambda x : (-x[2],-x[0],-x[1]))
    return eat

size = 2
a,b =0,0
for i in range(N):
    for j in range(N):
        if mat[i][j] == 9:
            a = i
            b = j
            break
time = 0
cnt = 0
while 1: # 계속해서 bfs를 돌려야한다, 왜냐하면 이동헤서 또 최단거리 찾아야하기 때문
    eat = bfs(a,b,size)
    if len(eat) == 0:
        break
    nx,ny,dist = eat.pop()
    
    time += dist
    mat[a][b] = 0
    mat[nx][ny] = 0
    a,b = nx,ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
print(time)  



