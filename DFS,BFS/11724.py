import sys
sys.setrecursionlimit(10000)
N,M = map(int,sys.stdin.readline().split())

visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]
def dfs(graph,start,visited):
    visited[start] = 1
    
    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph,i,visited)

for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
cnt = 0
for i in range(1,N+1): 
    if visited[i] == 0:
        dfs(graph,i,visited)
        cnt += 1
        
print(cnt)

        
        
        