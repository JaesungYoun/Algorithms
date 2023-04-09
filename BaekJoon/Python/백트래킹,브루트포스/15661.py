import sys

N = int(sys.stdin.readline())

s = []

for _ in range(N):
    s.append(list(map(int,sys.stdin.readline().split())))
diff = sys.maxsize

visited = [False] * N
def dfs(depth,idx,n):
    global diff
    if depth == n: 
        start = 0
        link = 0
                
        for i in range(N):
            if visited[i]:
                for j in range(i+1,N):
                    if visited[j]:
                        start += s[i][j]
                        start += s[j][i]
            else:
                for j in range(i+1,N):
                    if not visited[j]:
                        link += s[i][j]
                        link += s[j][i]
    
        diff = min(diff,abs(start - link))
        if diff == 0:
            return
        return
    
    for i in range(idx,N):
        if visited[i]:
            continue
        visited[i] = True
        dfs(depth+1,i+1,n)
        visited[i] = False
for i in range(N//2,0,-1):
    dfs(0,0,i)
    if diff == 0:
        break
    
print(diff)