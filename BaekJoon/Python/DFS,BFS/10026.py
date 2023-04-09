import sys
import copy
sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())

mat = []
for _ in range(N):
    mat.append(list(sys.stdin.readline().rstrip()))

mat2 = copy.deepcopy(mat)


for i in range(len(mat2)):
    for j in range(len(mat2[i])):
        if mat2[i][j] == "R":
            mat2[i][j] = "G"

def dfs(x,y,color,graph,visited):
    if not(0<=x<N and 0<=y<N):
        return False
    
    if visited[x][y] == 0 and graph[x][y] == color:
        visited[x][y] = 1
        dfs(x+1,y,color,graph,visited)
        dfs(x-1,y,color,graph,visited)
        dfs(x,y+1,color,graph,visited)
        dfs(x,y-1,color,graph,visited)
        return True
    return False

r = 0
g = 0 
b = 0
r_blind = 0
g_blind = 0
b_blind = 0
visited = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        
        if dfs(i,j,mat[i][j],mat,visited) == True:
            if mat[i][j] == "R":
                r += 1
            elif mat[i][j] == "G":
                g += 1
            else:
                b += 1
        if dfs(i,j,mat2[i][j],mat2,visited2) == True:
            if mat2[i][j] == "R":
                r_blind += 1
            elif mat2[i][j] == "G":
                g_blind += 1
            else:
                b_blind += 1

normal = r + g + b
blind = r_blind + g_blind + b_blind
print(normal,blind)