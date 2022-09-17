import sys

N,M = map(int,sys.stdin.readline().split())

nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
arr = []
visited = [False] * N
def dfs(depth):
    if depth == M:
        print(*arr)
        return
    
    last = 0
    for i in range(N):
        
        if last != nums[i]:
            arr.append(nums[i])
            last = nums[i]
            dfs(depth + 1)
            arr.pop()
            
            
        
dfs(0)
    
    