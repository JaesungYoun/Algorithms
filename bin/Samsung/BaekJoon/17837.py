N,K = map(int,input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))

chess = [[[] for _ in range(N)] for _ in range(N)]

horse = []
for i in range(K):
    r,c,d = map(int,input().split())
    horse.append([r-1,c-1,d-1])
    chess[r-1][c-1].append(i)
# 동 서 북 남 
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def change_dir(d): # 방향 전환 함수
    if d in [0,2]:
        d += 1
    elif d in [1,3]:
        d -= 1
    return d

def move(h_num): # 말이 움직이는 함수
    x,y,d = horse[h_num]
    nx = x + dx[d]
    ny = y + dy[d]
    
    if not (0<=nx<N and 0<=ny<N) or mat[nx][ny] == 2:
        d = change_dir(d)
        horse[h_num][2] = d
        nx = x +dx[d]
        ny = y +dy[d]

        if not (0<=nx<N and 0<=ny<N) or mat[nx][ny] == 2:
            return True
        
    idx = 0 
    for i,h_n in enumerate(chess[x][y]):
        if h_n == h_num:
            idx = i
            break
    
    if mat[nx][ny] == 1:
        chess[x][y][idx:] = list(reversed(chess[x][y][idx:]))
    chess[nx][ny].extend(chess[x][y][idx:])
    for h in chess[x][y][idx:]:
        horse[h][0] = nx
        horse[h][1] = ny 
    chess[x][y] = chess[x][y][:idx]   
    
    if len(chess[nx][ny]) >= 4:
        return False
    return True

cnt = 0 # 턴

while 1:
    flag = False

    if cnt > 1000:
        print(-1)
        break
    for i in range(K):
        if move(i) == False:
            flag = True
            break
    cnt += 1
    if flag:
        print(cnt)
        break
    

