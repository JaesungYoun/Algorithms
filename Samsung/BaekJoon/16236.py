from collections import deque

N = int(input())

mat = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,size): # bfs (최단거리 물고기 찾기) - visited 배열에 거리들을 기록! 
    queue = deque([(x,y)])
    visited = [[-1] * N for _ in range(N)]
    visited[x][y] = 0

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == -1:
                if mat[nx][ny] <= size: # 이동 
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
    return visited

def solve(visited,size):
    x,y = 0,0
    min_dist = 1e9
    for i in range(N):
        for j in range(N):
            if visited[i][j] != -1 and size > mat[i][j] >= 1 :
                if min_dist > visited[i][j]:
                    min_dist = visited[i][j]
                    x = i
                    y = j

    if min_dist == 1e9:
        return False
    else:
        return x,y,min_dist



# 상어 위치 찾기 

shark_x,shark_y = 0,0
shark_size = 2
for i in range(N):
    for j in range(N):
        if mat[i][j] == 9:
            shark_x = i
            shark_y = j 
            mat[shark_x][shark_y] = 0
            break

time = 0
cnt = 0
# 시간 재기
while 1: 
    v = bfs(shark_x,shark_y,shark_size) # 해당 위치에서부터 모든 물고기까지의 거리 구하기
    result= solve(v,shark_size) # 구한 물고기의 거리들로부터 최단거리 물고기 좌표 리턴 
    
    if not result: # 한 마리도 없으면 
        print(time)
        break
    else: # 한 마리라도 있으면 
        shark_x,shark_y = result[0],result[1]
        time += result[2]
        mat[shark_x][shark_y] = 0
        cnt += 1 # 물고기 한 마리 먹음

    if cnt == shark_size:
        shark_size += 1
        cnt = 0
