import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(start,depth):
    visited[start] = True
    if depth == 2:
        return
    
    for i in graph[start]:
        dfs(i,depth + 1)
            
            

dfs(1,0)

print(visited.count(True) - 1)

