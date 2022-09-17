import sys
from collections import deque
M,N,K = map(int,sys.stdin.readline().split())


visited = [[0] * M for _ in range(N)]

for _ in range(K):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            visited[i][j] = 1
        
dx = [-1,1,0,0]
dy = [0,0,-1,1]
        
def bfs(x,y):
    global area
    q = deque()
    q.append([x,y])
    
    while q:
        a,b = q.popleft()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if (0 <= nx < N and 0 <= ny < M) and visited[nx][ny] == 0:
                q.append([nx,ny])
                visited[nx][ny] = 1 
                area += 1

areas = []
for i in range(N):
    for j in range(M):
        area = 1
        if visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i,j)
            areas.append(area)
print(len(areas))
print(*sorted(areas))