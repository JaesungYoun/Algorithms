from collections import deque
N,M = map(int,input().split())



mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    global answer
    tmp_mat = [i[:] for i in mat]
    
    queue = deque() # 바이러스 위치를 모두 담아놓음 
    for x in range(N):
        for y in range(M):
            if tmp_mat[x][y] == 2:
                queue.append((x,y))

    while queue: # 모두 동시에 움직여도 어차피 순서대로 해도 된다,
        # 왜냐하면 이전에 빈 칸은 이전 바이러스에 의해 전염될것이므로
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0 <=ny < M and tmp_mat[nx][ny] == 0:
                queue.append((nx,ny))
                tmp_mat[nx][ny] = 2

    cnt = 0
    for i in range(N):
        cnt += tmp_mat[i].count(0)
    answer = max(answer,cnt)


v = [[0] * M for _ in range(N)]
def backtracking(depth):
    if depth == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 0:
                if v[i][j] == 1:
                    continue
                v[i][j] = 1
                mat[i][j] = 1
                backtracking(depth+1)
                mat[i][j] = 0 
                v[i][j] = 0

answer = 0 
backtracking(0)
print(answer)



