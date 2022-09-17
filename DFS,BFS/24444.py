import sys
from collections import deque
N,M,R =map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

visited = [False] * (N+1)
cnt = 1
result = [0] * (N+1)
def bfs(graph,v,visited):
    global cnt
    queue = deque([v])
    visited[v] = True
    
    while queue:
        v = queue.popleft()
        result[v] = cnt
        cnt += 1
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph,R,visited)
for i in range(1,N+1):
    print(result[i])