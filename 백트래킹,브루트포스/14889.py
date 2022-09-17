import sys

N = int(sys.stdin.readline())



stats = []

for i in range(N):
    stats.append(list(map(int,sys.stdin.readline().split())))
    

visited = [False] * N

diff = sys.maxsize


def dfs(depth,idx):
    global diff
    if depth == N//2:
        start = 0 
        link = 0
    
        for i in range(N):
            if visited[i]:
                for j in range(i+1,N):
                    if visited[j]:
                        start += stats[i][j]
                        start += stats[j][i]
            else:
                for j in range(i+1,N):
                    if not visited[j]:
                        link += stats[i][j]
                        link += stats[j][i]
    
        diff = min(diff,abs(start - link))
        if diff == 0:
            return
        return
                    
    
    for i in range(idx,N):
        if visited[i]:
            continue
        visited[i] = True
        dfs(depth + 1,i + 1)
        visited[i] = False
        
dfs(0,0)
    
print(diff)
        
    
        