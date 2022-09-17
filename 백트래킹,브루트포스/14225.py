import sys

N =int(sys.stdin.readline())

s = list(map(int,sys.stdin.readline().split()))

visited = [0] * 2000000
def dfs(depth,sum):
    if depth == N:
        return
    
    sum += s[depth]
    visited[sum] = 1
    dfs(depth + 1,sum)
    dfs(depth+1,sum-s[depth])
    
        
dfs(0,0)

for i in range(1,len(visited)):
    if visited[i] == 0:
        print(i)
        break
    