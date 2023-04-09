import sys

N,M,x,y,K = map(int,sys.stdin.readline().split())

mat = []
for _ in range(N):
    mat.append(list(map(int,sys.stdin.readline().split())))

command = list(map(int,sys.stdin.readline().split()))

# 동,서,북,남
dx = [0,0,-1,1]
dy = [1,-1,0,0]
      #1,2,3,4,5,6
dice = [0,0,0,0,0,0]
# 동 : 4,2,1,6,5,3
# 서 : 3,2,6,1,5,4
# 남 : 5,1,3,4,6,2
# 북 : 2,6,3,4,1,5

def turn(dir):
    global dice
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else: #남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
        
def move(x,y):

    for c in command:
        nx = x + dx[c-1]
        ny = y + dy[c-1]
        if not(0<=nx<N and 0<=ny<M):
            continue
        
        turn(c)
        if mat[nx][ny] == 0:
            mat[nx][ny] = dice[5]
        else:
            dice[5] = mat[nx][ny]
            mat[nx][ny] = 0
            
        x,y = nx,ny
        print(dice[0])
        
move(x,y)