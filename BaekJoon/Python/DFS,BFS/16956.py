import sys

R,C = map(int,sys.stdin.readline().split())

pasture = []

for i in range(R):
    pasture.append(list(map(str,sys.stdin.readline().strip())))
    
    
# 좌,우,상,하
dx = [0,0,-1,1]
dy = [-1,1,0,0]

sign = False

for i in range(R):
    for j in range(C):
        if pasture[i][j] == 'W':
            for k in range(4):
                x = i + dx[k] # 행
                y = j + dy[k] # 열
                
                if not (0 <= x < R and 0 <= y < C):
                    continue
                
                if pasture[x][y] == "S":
                    sign = True
                    break

if sign:
    print(0)
else:
    print(1)
    
    for i in range(R):
        for j in range(C):
            if pasture[i][j] == '.':
                pasture[i][j] = "D"
    
    for i in pasture:
        print(''.join(i))
    