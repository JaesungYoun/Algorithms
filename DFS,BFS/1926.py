import sys
sys.setrecursionlimit(1000000)
n,m = map(int,sys.stdin.readline().split())

mat = []
for _ in range(n):
    mat.append(list(map(int,sys.stdin.readline().split())))
    
    
def dfs(x,y):
    global area
    if not (0<=x<n and 0<=y<m):
        return False
    
    if mat[x][y] == 1:
        area += 1
        mat[x][y] = 0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

cnt = 0
areas = []
for i in range(n):
    for j in range(m):
        area = 0
        if dfs(i,j) == True:
            cnt +=1
            areas.append(area)

print(cnt)
if areas:
    print(max(areas))
else:
    print(0)
        