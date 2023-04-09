import sys
from collections import deque

M,N = map(int,sys.stdin.readline().split())

mat = []

for _ in range(N):
    mat.append(list(map(int,sys.stdin.readline().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()

for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            queue.append((i,j))

def bfs():
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <=ny < M and mat[nx][ny] == 0:
                queue.append((nx,ny))
                mat[nx][ny] = mat[x][y] + 1
                
bfs()       
            
flag = False
result = 0

for i in range(N):
    for j in range(M):
        if mat[i][j] == 0:
            flag = True
            break
        result = max(result,mat[i][j])
        
if flag:
    print(-1)
else:
    print(result - 1)
        