import sys
from collections import deque
N,M,K,X = map(int,sys.stdin.readline().split())

path = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    path[a].append(b)
    
    
visited = [False] * (N+1)
cnt = [0] * (N+1)
def bfs(start):
   
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft();
        for i in path[v]:
            if visited[i] == False:
                visited[i] = True
                cnt[i] = cnt[v] + 1
                queue.append(i)

bfs(X)
if K in cnt:
    for i in range(1,N+1):
        if cnt[i] == K:
            print(i)
else:
    print(-1)
    
