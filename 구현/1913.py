import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

num = N ** 2
chart = [[0] * N for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

x = y = 0
chart[x][y] = num
num -= 1
res_X = res_Y = 0
while True:
    for i in range(4):
        while True:
            x += dx[i]
            y += dy[i]
            
            if x < 0 or x >= N or y < 0 or y >= N or (chart[x][y]):
                x -= dx[i]
                y -= dy[i]
                break
            
            else:
                chart[x][y] = num
                if chart[x][y] == M:
                    res_X = x
                    res_Y = y
                num -= 1
            
    if x == N // 2 and y == N//2:
        break
    
for i in chart:
    print(*i)
print(res_X + 1 ,res_Y + 1)
                
                
                
                