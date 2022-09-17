import sys
from collections import deque
T = int(sys.stdin.readline())

dx = [-2,-2,2,2,-1,-1,1,1]
dy = [-1,1,-1,1,2,-2,2,-2]

def bfs(x1,y1,x2,y2):
    
    queue = deque([])
    queue.append([x1,y1])
    graph[x1][y1] = 1
    
    while queue:
        x,y = queue.popleft()
        
        if x == x2 and y == y2:
            print(graph[x2][y2] - 1)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < l and 0 <= ny < l):
                continue
            
            if graph[nx][ny] == 0:
                queue.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1
                

for _ in range(T):
    l = int(sys.stdin.readline())
    x1,y1 = map(int,sys.stdin.readline().split())
    x2,y2 = map(int,sys.stdin.readline().split())
    graph = [[0] * l for i in range(l)]
    bfs(x1,y1,x2,y2)


