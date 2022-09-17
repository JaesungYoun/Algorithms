import sys
from collections import deque
N = int(sys.stdin.readline())

r1,c1,r2,c2 = map(int,sys.stdin.readline().split())

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

visited = [[0] * N for _ in range(N)]
flag =False
def bfs(x,y):
    global cnt,flag
    queue = deque([])
    queue.append((x,y))
    visited[x][y] = 1
    
    while queue:
        x,y = queue.popleft()

        if x == r2 and y == c2:
            flag = True
            return visited[x][y] - 1
            
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < N and 0<=ny<N and visited[nx][ny] == 0 :
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                       
                
cnt = 0
res = bfs(r1,c1)
if not flag:
    print(-1)           
else:
    print(res)
           
