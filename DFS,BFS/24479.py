import sys
sys.setrecursionlimit(100000)
N,M,R =map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
result = [0] * (N+1)
cnt = 1
def dfs(graph,v,visited):
    global cnt
    result[v] = cnt
    visited[v] = True
    
    for i in graph[v]:
        if visited[i] == False:
            cnt += 1
            dfs(graph,i,visited)
            
for i in graph:
    i.sort()

dfs(graph,R,visited)
for i in range(1,N+1):
    print(result[i])
    
print(result)