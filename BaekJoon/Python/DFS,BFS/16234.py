import sys
from collections import deque

N,L,R = map(int,sys.stdin.readline().split())

mat = []

for _ in range(N):
    mat.append(list(map(int,sys.stdin.readline().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[0] * N for _ in range(N)]

def bfs(x,y):
    global people
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    temp = []
    temp.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                if L <= abs(mat[nx][ny] - mat[x][y]) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    temp.append((nx,ny))
    return temp

cnt = 0
while 1: 
    flag = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N): # for 문 다 돌면 열릴 수 있는 모든 국가의 국경선이 열림
        for j in range(N):
            if visited[i][j] == 0:
                union = bfs(i,j)
                if len(union)> 1:
                    flag = 1 
                    people = sum([mat[x][y] for x,y in union]) // len(union)
                    
                    for x,y in union:
                        mat[x][y] = people
    if flag == 0:
        break
    cnt += 1
    
print(cnt)