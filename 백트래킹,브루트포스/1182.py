import sys

N,S = map(int,sys.stdin.readline().split())

nums = list(map(int,sys.stdin.readline().split()))
    
cnt = 0
result = []
visited = [False] * N 
def dfs(idx,sum):
    global cnt
    if idx == N:
        return
    
    sum += nums[idx]
    if sum == S:
        cnt += 1
    
    dfs(idx + 1, sum - nums[idx])
    dfs(idx + 1, sum)
    
    
dfs(0,0)
print(cnt)

        