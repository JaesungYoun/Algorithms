import sys
from collections import deque
N,M,V = map(int,sys.stdin.readline().split())


graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

visited = [False] * (N+1)
visited_bfs = [False] * (N+1)
def dfs(graph,v,visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph,i,visited)
            
def bfs(graph,start,visited):
    queue = deque([start])
    visited_bfs[start] = True
            
    while queue:
        v = queue.popleft()
        print(v,end = ' ')
        
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True
            
dfs(graph,V,visited)
print()
bfs(graph,V,visited_bfs)