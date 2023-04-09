from collections import deque
N,M = map(int,input().split())

r,c,d = map(int,input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))


# 북,동,남,서
dr = [-1,0,1,0]
dc = [0,1,0,-1]

def clean(r,c,dir):
    
    queue = deque()
    queue.append((r,c))
    mat[r][c] = 2
    d = dir
    while queue:
        flag = 1
        x,y = queue.popleft()
        
        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]
            
            if 0<=nr<N and 0<=nc<M:
                if mat[nr][nc] == 0:
                    flag = 0

        if not flag:
            for i in range(4):
                d = (d + 3) % 4 # 90도 회전
                nx = x + dr[d]
                ny = y + dc[d]
                if 0<=nx<N and 0<=ny <M and mat[nx][ny] == 0:
                    queue.append((nx,ny)) # 전진
                    mat[nx][ny] = 2
                    break
              
        else:
            nr = x + dr[(d+2) % 4]
            nc = y + dc[(d+2) % 4]
            if mat[nr][nc] == 1: # 후진했는데 벽
                return
            else: # 청소한 곳은 움직이기 가능 
                queue.append((nr,nc))

clean(r,c,d)
cnt = 0
for i in mat:
    cnt += i.count(2)

print(cnt)
