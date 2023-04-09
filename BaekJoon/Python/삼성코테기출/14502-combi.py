import sys
from collections import deque
import copy
from itertools import combinations
N,M = map(int,sys.stdin.readline().split())

mat = []
for _ in range(N):
    mat.append(list(map(int,sys.stdin.readline().split())))
empty = [(n, m) for n in range(N) for m in range(M) if mat[n][m] == 0]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0] * M for _ in range(N)]
def bfs():
    global result
    
    for wall_combi in combinations(empty, 3):
        queue = deque()
        
        new_mat = copy.deepcopy(mat)
        for i,j in wall_combi:
            new_mat[i][j] = 1
        
        temp = copy.deepcopy(new_mat)
        for x in range(N):
            for y in range(M):
                if temp[x][y] == 2:
                    queue.append((x,y))
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<N and 0<=ny<M and temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx,ny))
        cnt = 0
        for i in range(N):
            cnt += temp[i].count(0)
        result = max(result,cnt)
            
v = [[0] * M for _ in range(N)]
result = 0 
bfs()
print(result)