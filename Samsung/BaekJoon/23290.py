from collections import deque
import copy
M,S = map(int,input().split())

mat = [[[] for _ in range(4)] for _ in range(4)] # 격자
for i in range(1,M+1):
    f_x,f_y,d = map(int,input().split())
    mat[f_x-1][f_y-1].append(d-1) # 물고기 방향 저장
s_x,s_y = map(int,input().split()) # 상어 위치
s_x -= 1
s_y -= 1
# 물고기의 방향
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
# 상어의 방향
# 상 좌 하 우
s_dx = [-1,0,1,0]
s_dy = [0,-1,0,1]


smell = [[0 for _ in range(4)] for _ in range(4)]

def fish_move():
    new_mat = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            while temp[i][j]:
                d = temp[i][j].pop()
                for _ in range(8):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    if 0<=nx<4 and 0<=ny<4 and smell[nx][ny] == 0 and (not(nx==s_x and ny==s_y)):
                        new_mat[nx][ny].append(d)
                        break
                    else:
                        d = (d+7) % 8
                else: # 만약 이동하지 못했으면 원래 자리에 다시 넣어줘야함
                    new_mat[i][j].append(d)
    return new_mat


def dfs(cnt,x,y,total,visit):
    global max_eat,eat
    global s_x,s_y

    if cnt == 3:
        if max_eat < total:
            max_eat = total
            s_x = x
            s_y = y
            eat = visit[:]

        return

    for i in range(4):
        nx = x + s_dx[i]
        ny = y + s_dy[i]
        if 0<=nx<4 and 0<=ny<4:
            if (nx,ny) not in visit:
                visit.append((nx,ny))
                dfs(cnt+1,nx,ny,total+len(temp[nx][ny]),visit)
                visit.pop()
            else:
                dfs(cnt+1,nx,ny,total,visit)

for i in range(S): # S번 연습
    eat = []
    visit = []
    max_eat = -1
    # 1. 모든 물고기 복제
    temp = copy.deepcopy(mat)

    # 2. 물고기 이동
    temp = fish_move()

    # 3. 상어 이동
    dfs(0,s_x, s_y,0,visit)
    for x,y in eat:
        if temp[x][y]:
            temp[x][y] = []
            smell[x][y] = 3
    # 4. 냄새 사라짐
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1

    # 5. 복제
    for i in range(4):
        for j in range(4):
            mat[i][j] += temp[i][j]

answer = 0
for i in range(4):
    for j in range(4):
        answer += len(mat[i][j])
print(answer)




