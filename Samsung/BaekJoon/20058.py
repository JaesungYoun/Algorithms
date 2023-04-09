from collections import deque

N,Q = map(int,input().split())
mat = []
for _ in range(2**N):
    mat.append(list(map(int,input().split())))
stage = list(map(int,input().split()))
def divide_and_turn(L):
    divide_num = 2**L
    temp = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for i in range(0,2**N,divide_num):
        for j in range(0,2**N,divide_num):
            for k in range(divide_num):
                for m in range(divide_num):
                    temp[i+k][j+m] = mat[i + (2**L - 1 - m)][j + k]

    return temp
def melt():
    global mat
    temp = [[0 for _ in range(2**N)] for _ in range(2**N)]

    to_be_deleted = []

    for x in range(len(temp)):
        for y in range(len(temp[0])):
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<len(temp) and 0<=ny<len(temp[0]):
                    if mat[nx][ny] > 0:
                        cnt += 1

            if (x,y) not in to_be_deleted and cnt < 3:
                to_be_deleted.append((x,y))

    for a,b in to_be_deleted:
        mat[a][b] -= 1


    return mat

dung = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0 for _ in range(2**N)] for _ in range(2**N)]
def bfs(x,y):
    cnt = 1

    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<2**N and 0<=ny<2**N and visited[nx][ny] == 0:
                if mat[nx][ny] > 0:
                    cnt += 1
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
    return cnt



for L in stage:
    mat = divide_and_turn(L)
    mat = melt()

result1 = 0
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] >= 0:
            result1 += mat[i][j]

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] > 0:
            dung = max(dung,bfs(i,j))



print(result1)
print(dung)