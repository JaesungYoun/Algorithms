import sys
sys.setrecursionlimit(10000)

def dfs(x,y,w,h):

    if not (0 <= x < w and 0 <= y < h):
        return False
    
    if _map[x][y] == 1:
        _map[x][y] = 0
        
        # 상,하,좌,우,좌상,좌하,우상,우하
        dfs(x-1,y-1,w,h)
        dfs(x-1,y,w,h)
        dfs(x-1,y+1,w,h)
        dfs(x,y-1,w,h)
        dfs(x,y+1,w,h)
        dfs(x+1,y-1,w,h)
        dfs(x+1,y,w,h)
        dfs(x+1,y+1,w,h)
        return True
    return False
    
while 1: 
    w,h = map(int,sys.stdin.readline().split())
    if w == 0 and h == 0:
        break 
    _map = []
    cnt = 0 
    for i in range(h):
        _map.append(list(map(int,sys.stdin.readline().split())))
    
    
    
    for i in range(h):
        for j in range(w):
            if dfs(i,j,h,w) == True:
                cnt += 1
    print(cnt)
    
    
    
    
    
    
    
    
    
    
    
        
    
    