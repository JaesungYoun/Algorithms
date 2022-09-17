import sys
sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())

mat = []

for _ in range(N):
    mat.append(list(map(int,sys.stdin.readline().rstrip().split())))

blue = 0 
white = 0

def dfs(x,y,N):
    global blue,white
    
    
    num = mat[x][y]
    if N == 1:
        if num == 1:
            blue += 1
        
        else:
            white += 1
        return
    for i in range(x,x+N):
        for j in range(y,y+N):
            if num != mat[i][j]:
                for k in range(2):
                    for l in range(2):
                        dfs(x+k*(N//2),y+l*(N//2),N//2)     
                return
    
    if num == 1:
        blue += 1
        
    else:
        white += 1
        

dfs(0,0,N)
print(white)
print(blue)