from collections import deque
def solution(maps):
    answer = 0
    
    answer = bfs(maps,1,1)
    
    
    return answer

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(maps,x,y):
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * (m+1) for _ in range(n+1)]
    queue = deque()
    queue.append((x,y))
    
    
    visited[x][y] = 1
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 1<=nx<n+1 and 1<=ny<m+1:
                if maps[nx-1][ny-1] == 1 and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    
    if visited[n][m] == 0:
        return -1
        
    return (visited[n][m])
                
    
    
    