import sys
import copy
R,C = map(int,sys.stdin.readline().split())

mat = []

for i in range(R):
    mat.append(list(map(str,sys.stdin.readline().rstrip())))

result = copy.deepcopy(mat)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(R):
    for j in range(C):
        if mat[i][j] == "X":
            cnt = 0 
            for k in range(4):
                
                nx = i + dx[k]
                ny = j + dy[k]
                if not(0<=nx<R and 0<=ny<C):
                    cnt += 1
                    continue           
                if mat[nx][ny] == ".":
                    cnt += 1
            
            if cnt >= 3:
                result[i][j] = "."
    
start_x=0
end_x=0
    
for i in range(R):
    if 'X' in result[i]:
        start_x= i
        break
for i in range(R-1,-1,-1):
    if 'X' in result[i]:
        end_x = i
        break

temp = []
for i in range(start_x,end_x+1):
    for j in range(C):
        if 'X' == result[i][j]:
            temp.append(j)
            
temp = sorted(list(set(temp)))
for i in range(start_x,end_x+1):
    print("".join(result[i][temp[0]:temp[-1]+1]))