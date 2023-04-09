from collections import deque
N,L,R = map(int,input().split())
mat = []

for _ in range(N):
    mat.append(list(map(int,input().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    
    queue = deque()
    queue.append((x,y))
    temp = deque()
    visited[x][y] = 1
    temp.append((x,y))
    while queue:    
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0<=nx < N and 0<= ny < N and visited[nx][ny] == 0:
                if L <= abs(mat[x][y] - mat[nx][ny]) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    temp.append((nx,ny))
    return temp

cnt = 0
while 1:
    flag = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                union = bfs(i,j)
                if len(union) > 1:
                    people = sum([mat[x][y] for x,y in union]) // len(union)         

                    for ux,uy in union:
                        mat[ux][uy] = people
                    flag = 1

    if flag == 0:
        break
    cnt += 1

print(cnt)
