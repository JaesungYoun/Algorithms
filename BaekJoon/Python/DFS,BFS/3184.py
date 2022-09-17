import sys
sys.setrecursionlimit(100000)
r,c = map(int,sys.stdin.readline().split())

mat = []

for _ in range(r):
    mat.append(list(map(str,sys.stdin.readline().rstrip())))

def dfs(x,y):
    global s,w
    if not (0<=x<r and 0<=y<c):
        return False
    
    if mat[x][y] != "#":
        if mat[x][y] == "o":
            s += 1
        elif mat[x][y] == "v":
            w += 1
        
        mat[x][y] = "#"
        
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False
          
sheep = 0
wolf = 0
for i in range(r):
    for j in range(c):
        s = 0
        w = 0
        dfs(i,j)
        if s > w:
            sheep += s
        else:
            wolf += w
                
print(sheep,wolf)