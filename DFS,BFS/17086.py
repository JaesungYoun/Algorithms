import sys
from collections import deque


dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0:                
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])


n, m = map(int, sys.stdin.readline().split())

visited = []
queue = deque([])
for i in range(n):
    graph = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if graph[j] == 1:
            queue.append([i, j])
    visited.append(graph)

bfs()

# 이동 거리에 최대 값을 구하고 처음 시작값을 뺀다.
dist = 0
for i in range(n):
    for j in range(m):
        dist = max(dist, visited[i][j])
print(dist - 1)