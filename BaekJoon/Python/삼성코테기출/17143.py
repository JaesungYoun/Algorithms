R,C,M = map(int,input().split())
mat = [[0] * (C+1) for _ in range(R+1)]
for _ in range(M):
    r, c, s, d, z = map(int,input().split())
    mat[r][c] = [s,d-1,z]
# 상 하 우 좌
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def move():
    temp = [[0] * (C+1) for _ in range(R+1)]
    for i in range(1,R+1):
        for j in range(1,C+1):
            if mat[i][j] != 0:
                nx,ny,s,d,z = i,j,mat[i][j][0],mat[i][j][1],mat[i][j][2] 
                while s > 0:
                    nx += dx[d]
                    ny += dy[d]
                    if 1<=nx<R+1 and 1<=ny<C+1:
                        s-=1
                    else:
                        nx -= dx[d]
                        ny -= dy[d]
                        if d == 0: d = 1
                        elif d == 1: d = 0
                        elif d == 2: d = 3
                        elif d == 3: d = 2
                if temp[nx][ny] == 0:
                     temp[nx][ny] = [mat[i][j][0],d,z]
                else:
                    if temp[nx][ny][2] < z: # 크기가 원래있던 것보다 크면
                        temp[nx][ny] = [mat[i][j][0],d,z]
    return temp

result = 0 
for i in range(1,C+1):
    for j in range(1,R+1): # 열 행 바꿔서 하는 거 주의!
        if mat[j][i] != 0: # 가장 가까운 상어 먹기
            result += mat[j][i][2]
            mat[j][i] = 0
            break # break 해줘야 가장 가까운 상어만 먹고 그만둚
    mat = move()
print(result)
            