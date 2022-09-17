import sys

n = int(sys.stdin.readline())

p = int(sys.stdin.readline())

com = [[] for _ in range(n+1)]
visited = [0] * n

def dfs(graph,v,visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph,i,visited)

for i in range(p):
    c1,c2 = map(int,sys.stdin.readline().split())
    com[c1].append(c2)
    com[c2].append(c1)

dfs(com,1,visited)
print(sum(visited)-1)
