import sys
from collections import deque
M,N,H = map(int,sys.stdin.readline().split())

tomato = []

queue = deque()
for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(M):
            if temp[j][k] == 1:
                queue.append((i,j,k))
    tomato.append(temp)
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
    
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if 0<=nx<N and 0<=ny<M and 0<=nz<H and tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = tomato[z][x][y] + 1
                queue.append((nz,nx,ny))
bfs()

flag = False
result = 0
for i in range(len(tomato)):
    for j in range(len(tomato[i])):
        for k in range(len(tomato[i][j])):
            if tomato[i][j][k] == 0:
                flag = True
                break
            result = max(result,tomato[i][j][k])
if flag:
    print(-1)
else:
    print(result - 1)