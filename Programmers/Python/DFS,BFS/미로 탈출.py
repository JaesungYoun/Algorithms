from collections import deque
def solution(maps):
    answer = 0
    
    r = len(maps)
    c = len(maps[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    def bfs(x,y,end_x,end_y):
        visited = [[0 for _ in range(c)] for _ in range(r)]
        queue = deque()
        queue.append((x,y))
        visited[x][y] = 1
        
        while queue:
            x,y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<r and 0<=ny<c and visited[nx][ny] == 0:
                    if maps[nx][ny] != 'X':
                        queue.append((nx,ny))
                        visited[nx][ny] = visited[x][y] + 1
                        
        return visited[end_x][end_y] - 1
        
    s_x,s_y,l_x,l_y = -1,-1,-1,-1
    e_x,e_y = -1,-1
    for i in range(r):
        for j in range(c):
            if maps[i][j] == 'S':
                s_x = i
                s_y = j
            elif maps[i][j] == 'L':
                l_x = i
                l_y = j
            elif maps[i][j] == 'E':
                e_x = i
                e_y = j
    
    t1 = bfs(s_x,s_y,l_x,l_y)
    if t1 == -1:
        return -1
    t2 = bfs(l_x,l_y,e_x,e_y)
    if t2 == -1:
        return -1
    
    answer = t1 + t2
    
    return answer