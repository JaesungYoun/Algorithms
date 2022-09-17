import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        target = queue.popleft()

        # 친구 관계를 확인하고 탐색하지 않은 친구라면 탐색한다.
        for i in graph[target]:
            if not visited[i]:
                # 탐색하기 위한 횟수를 체크한다.
                visited[i] = visited[target] + 1
                queue.append(i)

    
res = []
for i in range(1,N+1):
    visited = [0] * (N+1)
    bfs(i)
    res.append(sum(visited))

print(res.index(min(res))+1)