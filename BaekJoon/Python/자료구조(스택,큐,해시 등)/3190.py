import sys
from collections import deque
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
mat = [[0] * (N) for _ in range(N)]
for _ in range(K):
    r,c = map(int,sys.stdin.readline().split())
    mat[r-1][c-1] = 2
    
L = int(sys.stdin.readline())

info = deque()
for _ in range(L):
    X,C = map(str,sys.stdin.readline().split())
    X = int(X)
    info.append([X,C])

    #동,남,서,북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

time = 1
def move():
    x,y,d = 0,0,0
    queue = deque()
    queue.append((x,y))
    global time
    while 1:
        nx,ny = x + dx[d], y+dy[d]
        
        if not (0<=nx<N and 0<=ny<N) :
            break
        if ((nx,ny)) in queue:
            break
        
        queue.append((nx,ny))
        if mat[nx][ny] != 2:
            queue.popleft()
        else:
            mat[nx][ny] = 0
        
        if len(info) > 0:
            if info[0][0] == time:
                if info[0][1] == 'L':
                    d = (d+3) % 4
                else:
                    d = (d+1) % 4
                info.popleft()
        time += 1 
        x,y = nx,ny
        
move()        
print(time)    
    