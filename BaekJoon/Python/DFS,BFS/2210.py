import sys

mat = []
for _ in range(5):
    mat.append(list(map(str,sys.stdin.readline().split())))
    
dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1] 
result = []
def dfs(x,y,num):
    if len(num) == 6:
        if num not in result:
            result.append(num)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx,ny,num+mat[nx][ny])


for i in range(5):
    for j in range(5):
        dfs(i,j,mat[i][j])
        
print(len(result))
