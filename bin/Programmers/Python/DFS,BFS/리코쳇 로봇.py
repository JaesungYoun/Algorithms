from collections import deque
def solution(board):
    answer = 0
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    visited = [[-1 for _ in range(len(board[0]))] for _ in range(len(board))]
    r_x,r_y = 0,0
    g_x,g_y = -1,-1
    def bfs(x,y):
    
        queue = deque()
        queue.append((x,y))
        visited[x][y] = 0
        
        while queue:
            x,y = queue.popleft()
            
        
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                while 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny] != 'D':
                    nx += dx[i]
                    ny += dy[i]
                
                nx -= dx[i]
                ny -= dy[i]
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
        
        return visited[g_x][g_y]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                r_x = i
                r_y = j
            if board[i][j] == 'G':
                g_x = i
                g_y = j

    answer = bfs(r_x,r_y)
    print(visited)
    return answer