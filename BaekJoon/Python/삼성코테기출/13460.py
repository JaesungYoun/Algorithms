import sys
from collections import deque 

N,M = map(int,sys.stdin.readline().split())

mat = []
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
for i in range(N):
    mat.append(list(input()))

for i in range(N):
    for j in range(M):
        if mat[i][j] == "R":
            rx = i
            ry = j
        elif mat[i][j] == "B":
            bx = i
            by = j

def bfs(rx,ry,bx,by):
    queue = deque()
    queue.append((rx,ry,bx,by))
    visited[rx][ry][bx][by] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    cnt = 0 
    while queue:
        for _ in range(len(queue)):
            rx,ry,bx,by = queue.popleft()
            if cnt > 10:
                print(-1)
                return
            if mat[rx][ry] == 'O': # 현재 빨간 구슬의 위치가 구멍이라면 count출력
                print(cnt)
                return 
            for i in range(4): # 4방향 탐색
                nrx, nry = rx, ry
                while True: # #일 때까지 혹은 구멍일 때까지 움직임
                    nrx += dx[i]
                    nry += dy[i]
                    if mat[nrx][nry] == '#': # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if mat[nrx][nry] == 'O':
                        break
                nbx, nby = bx, by
                while True: # #일 때까지 혹은 구멍일 때까지 움직임
                    nbx += dx[i]
                    nby += dy[i]
                    if mat[nbx][nby] == '#': # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if mat[nbx][nby] == 'O':
                        break
                if mat[nbx][nby] == 'O': # 파란구슬이 먼저 구멍에 들어가거나 동시에 들어가면 안됨 따라서 이 경우 무시
                    continue
                if nrx == nbx and nry == nby: # 두 구슬의 위치가 같다면
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby))
        cnt += 1        
    print(-1) # 10회가 초과하지 않았지만 10회 내에도 구멍에 들어가지 못하는 경우
    return

bfs(rx,ry,bx,by)