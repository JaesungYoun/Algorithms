import sys

R,C,T = map(int,sys.stdin.readline().split())
mat = []

for _ in range(R):
    mat.append(list(map(int,sys.stdin.readline().split()))) 
    
for i in range(R):
    if mat[i][0] == -1:
        top = i
        bottom = i + 1
        break
    
    

def spread():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[0] * C for _ in range(R)]
    
    for x in range(R):
        for y in range(C):
            if mat[x][y] == 0 or mat[x][y] == -1:
                continue
            
            spread_dust = mat[x][y] // 5

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < R and 0 <= ny < C and mat[nx][ny] != -1:
                    visited[nx][ny] += spread_dust
                    visited[x][y] -= spread_dust
    for i in range(R):
        for j in range(C):
            mat[i][j] += visited[i][j]

def clean_top():
    
    # 반시계 방향으로
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    x,y,direction = top,1,0
    prev = 0
    
    while 1:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if x == top and y == 0: # 공기청정기로 돌아오면 break
            break
        if not (0<=nx < R and 0<=ny<C):
            direction += 1 # 방향전환
            continue
        
        mat[x][y], prev = prev, mat[x][y]
        x,y = nx,ny
    
def clean_bottom():
     # 시계 방향으로
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x,y,direction = bottom,1,0
    prev = 0
    
    while 1:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if x == bottom and y == 0: # 공기청정기로 돌아오면 break
            break
        if not (0<=nx < R and 0<=ny<C):
            direction += 1 # 방향전환
            continue
        
        mat[x][y], prev = prev, mat[x][y]
        x,y = nx,ny
        


for _ in range(T):
    spread()
    clean_top()
    clean_bottom()
    
print(sum(map(sum, mat)) + 2) # 공기청소기 -1 2개인부분을 더해줘야함

    
    