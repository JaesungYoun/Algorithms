import sys

N = int(sys.stdin.readline())

values = []

for i in range(N):
    values.append(list(map(int,sys.stdin.readline().split())))
    
dx = [-1,1,0,0,0]
dy = [0,0,-1,1,0]
visited = [[0] * N for _ in range(N)]

def check(x,y):
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0<=nx<N and 0<=ny<N) or visited[nx][ny] :
            return False
    return True

result = 1e9
def dfs(cost,cnt):
    global result
    if cost >= result:
        return 
    if cnt == 3:
        result = min(result,cost)
    for i in range(1,N-1):
        for j in range(1,N-1):
            if check(i,j):
                temp = 0
                for k in range(5):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    visited[nx][ny] = 1
                    temp += values[nx][ny]
                dfs(cost+temp,cnt+1)
                for k in range(5):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    visited[nx][ny] = 0    
dfs(0,0)
print(result)
        
    
