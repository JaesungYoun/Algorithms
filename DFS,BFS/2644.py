import sys
from collections import deque

N = int(sys.stdin.readline())

a,b = map(int,sys.stdin.readline().split())

m = int(sys.stdin.readline())

relations = [[] for _ in range(N+1)]
result = [0] * (N+1)
for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    relations[x].append(y)
    relations[y].append(x)
    

visited = [False] * (N+1)
def dfs(relations,start,visited):
    visited[start] = True
    
    for i in relations[start]:
        if visited[i] == False:
            result[i] = result[start] + 1
            dfs(relations,i,visited)
    
dfs(relations,a,visited)
if result[b] > 0:
    print(result[b])
else:
    print(-1)
    
    



            
            
            