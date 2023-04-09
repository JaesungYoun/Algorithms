from collections import deque
R,C,T = map(int,input().split())

a = [list(map(int,input().split()))for _ in range(R)]

# 공기청정기 좌표 구하기
for i in range(R):
    if a[i][0] == -1:
        top = i
        bottom = i + 1
        break


def spread(): # 미세먼지 확산
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[0] * C for _ in range(R)] 
    for x in range(R):
        for y in range(C):
            if a[x][y] == 0 or a[x][y] == -1:
                continue
            
            spread_dust = a[x][y] // 5 # 확산되는 미세먼지 양

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<R and 0<=ny<C and a[nx][ny] != -1: # visited는 안넣어줘도됨 중복해서 미세먼지 더해지기 가능하므로
                    visited[nx][ny] += spread_dust # 미세먼지 양 더해줌
                    visited[x][y] -= spread_dust

    for i in range(R):
        for j in range(C):
            a[i][j] += visited[i][j]

    
    
def clean_top():
    # 반시계 방향으로
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    x,y,direction = top,1,0 # 2열부터 시작해야하므로 y 좌표는 1 
    prev = 0 # 이전 값

    while 1:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if x == top and y == 0: # 공기청정기로 돌아오면 break
            break
        if not (0 <= nx < R and 0 <= ny < C):
            direction += 1 # 방향 전환
            continue

        a[x][y], prev = prev, a[x][y]
        x,y = nx,ny





def clean_bottom():
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    prev = 0
    x,y,direction = bottom,1,0

    while 1:

        nx = x + dx[direction]
        ny = y + dy[direction]

        if x == bottom and y == 0:
            break

        if not (0<=nx<R and 0<=ny<C):
            direction += 1
            continue

        a[x][y], prev = prev, a[x][y]
        x,y = nx,ny

for _ in range(T):
    spread()
    clean_top()
    clean_bottom()

result = 0
for i in range(R):
    for j in range(C):
        if a[i][j] != 0 or a[i][j] != -1:
            result += a[i][j]
    
print(result)