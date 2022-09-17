import sys
sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())


mat = []

for  _ in range(N):
    mat.append(list(map(int,sys.stdin.readline().split())))


    
def dfs(x,y):
    if not (0<=x<N and 0<=y<N):
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
    
max_val = 0
for i in range(len(mat)):
    for j in range(len(mat[i])):
        max_val = max(max_val,mat[i][j])

res = 0
for l in range(max_val + 1):
    cnt = 0
    graph = [[0] * N for _ in range(N)]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > l:
                graph[i][j] = 1
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if dfs(i,j) == True:
                cnt += 1
    
    res = max(cnt,res)
    
print(res)