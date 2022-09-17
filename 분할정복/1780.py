import sys

N = int(sys.stdin.readline())

mat = []

for _ in range(N):
    mat.append(list(map(int,sys.stdin.readline().rstrip().split())))

cnt1 = 0
cnt2 = 0
cnt3 = 0
  

def dfs(x,y,N):
    global cnt1,cnt2,cnt3
    
    num = mat[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if mat[i][j] != num:
                for k in range(3):
                    for l in range(3):
                        dfs(x+k*(N//3),y+l*(N//3),N//3)
                return
            
    if num == -1:
        cnt1 += 1
    elif num == 0:
        cnt2 += 1
    else:
        cnt3 += 1
        
        
dfs(0,0,N)
print(cnt1)
print(cnt2)
print(cnt3)