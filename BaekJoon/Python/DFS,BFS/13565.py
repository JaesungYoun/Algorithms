import sys
sys.setrecursionlimit(10000)
M,N= map(int,sys.stdin.readline().split())

mat = []

for _ in range(M):
    mat.append(list(map(int,sys.stdin.readline().rstrip())))
    

def dfs(x,y):
    global ans
    if x == M-1:
       ans = "YES"
       return 
    
    if not(0<=x<M and 0<=y<N):
        return
    
    
    if mat[x][y] == 0:
        mat[x][y] = 1
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
    

ans = 'NO'
for i in range(N):
    dfs(0,i)
    
print(ans)