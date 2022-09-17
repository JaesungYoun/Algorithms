import sys

N = int(sys.stdin.readline())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))
    
mat = [[] for _ in range(N)]
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            mat[i].append(j)
            mat[j].append(i)
    
    



def dfs(v):
    
    for i in mat[v]:
        if visited[i] == False and graph[v][i] == 1:
            visited[i] = True
            dfs(i)

        
visited = [False] * N
for i in range(N):
    dfs(i)
    for j in range(N):
        if visited[j] == True:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visited = [False] * N