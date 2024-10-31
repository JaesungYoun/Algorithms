from collections import deque
arr = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[1,0,0,1]]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    global arr
    queue = deque()
    queue.append((x,y))
    arr[x][y] = 0
    overlap_edge = 0
    cnt = 1
    
    while queue:
        x,y = queue.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0<=nx<len(arr) and 0<=ny<len(arr[i]):
                if arr[nx][ny] == 1:
                    queue.append((nx,ny))
                    arr[nx][ny] = 0
                    cnt += 1
                    overlap_edge += 1
                else:
                    if (nx,ny) in queue:
                        overlap_edge += 1
    cnt = 4*cnt
    l = (cnt - (2*overlap_edge))
    return l
    
max_len = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            isl_len = bfs(i,j)
            max_len = max(max_len,isl_len)
            

print(max_len)
