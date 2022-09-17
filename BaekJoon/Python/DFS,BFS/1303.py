import sys
sys.setrecursionlimit(100000)
N,M =map(int,sys.stdin.readline().split())

mat = []

for _ in range(M):
    mat.append(list(map(str,sys.stdin.readline().rstrip())))
    
visited = [[0] * N for _ in range(M)]
def dfs1(x,y):
    global w,b
    if not (0<=x<M and 0<=y<N):
        return False
    if mat[x][y] == "W" and visited[x][y] == 0:
        visited[x][y] = 1
        w+= 1
        dfs1(x+1,y)
        dfs1(x-1,y)
        dfs1(x,y+1)
        dfs1(x,y-1)
        return True
    return False

def dfs2(x,y):
    global w,b
    if not (0<=x<M and 0<=y<N):
        return False
    if mat[x][y] == "B" and visited[x][y] == 0:
        visited[x][y] = 1
        b+= 1
        dfs2(x+1,y)
        dfs2(x-1,y)
        dfs2(x,y+1)
        dfs2(x,y-1)
        return True
    return False
me = 0
you = 0
for i in range(M):
    for j in range(N):
        w,b = 0,0
        if mat[i][j] == "W" and dfs1(i,j): 
            me += pow(w,2)
        elif mat[i][j] == "B" and dfs2(i,j):
            you += pow(b,2)
print(me,you)