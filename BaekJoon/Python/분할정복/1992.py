import sys


N = int(sys.stdin.readline())

mat = []

for _ in range(N):
    mat.append(list(map(int,sys.stdin.readline().rstrip())))
    
result = ""
def dfs(x,y,N):
    global result
    
    
    num = mat[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if num != mat[i][j]:
                result += "("
                for k in range(2):
                    for l in range(2):
                        dfs(x+k*(N//2),y+l*(N//2),N//2)
                result += ")"
                return    
    
    if mat[x][y] == 1:
        result += "1"
    elif mat[x][y] == 0:
        result += "0"

dfs(0,0,N)

print(result)

