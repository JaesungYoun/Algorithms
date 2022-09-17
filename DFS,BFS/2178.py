import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

mat = []

for _ in range(N):
    a = list(map(str,sys.stdin.readline().strip()))
    a = list(map(int,a))
    mat.append(a)


visited = [[0] * M for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    
    
    queue = deque([(x,y)])
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if not (0<=nx<N and 0<=ny<M):
                continue
            
            if mat[nx][ny] == 1:
                mat[nx][ny] = mat[x][y] + 1
                queue.append((nx,ny))
                
    return mat[N-1][M-1]

print(bfs(0,0))
                
