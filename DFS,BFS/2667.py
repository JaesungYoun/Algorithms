import sys
sys.setrecursionlimit(1000000)
N = int(sys.stdin.readline())

mat = []

for i in range(N):
    a = list(map(str,sys.stdin.readline().rstrip()))
    a = list(map(int,a))
    mat.append(a)


def dfs(x,y):
    
    global cnt
    if not(0<=x<N and 0<=y<N):
        return
    
    if mat[x][y] == 1:
        cnt += 1
        mat[x][y] = 0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        
        return True
    return False
danji = 0
result = []
for i in range(N):
    for j in range(N):
        cnt = 0
        if dfs(i,j) == True:
            danji += 1
            result.append(cnt)

print(danji)
result.sort()
for i in result:
    print(i)  
    
