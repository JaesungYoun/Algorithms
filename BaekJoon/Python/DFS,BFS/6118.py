import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
        
def bfs(start):
    queue = deque([])
    queue.append(start)
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if visited[i] == 0 and i != 1:
                queue.append(i)
                visited[i] += visited[v] + 1
    
bfs(1)
print(visited.index(max(visited)),visited[visited.index(max(visited))],visited.count(max(visited)))
                
                