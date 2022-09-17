import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[b].append(a)
    
def bfs(v):
    
    q = deque([])
    q.append(v)
    visited[v] = True
    
    while q:
        c = q.popleft()
        for i in graph[c]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                
result = []
res = 0
for i in range(1,N+1):
    visited = [False] * (N+1)
    bfs(i)
    result.append(visited.count(True))
    
for i,v in enumerate(result):
    if v == max(result):
        print(i+1, end = " ")
        
