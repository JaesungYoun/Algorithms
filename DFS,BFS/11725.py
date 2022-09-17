import sys
sys.setrecursionlimit(10000)
N = int(sys.stdin.readline())

graph = [[]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
  
def dfs(graph,start,visited):
    for i in graph[start]:
        if visited[i] == 0:
            visited[i] = start
            dfs(graph,i,visited)

dfs(graph,1,visited)


for i in range(2,N+1):
    print(visited[i])