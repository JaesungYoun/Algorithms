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
        if visited[i] == True:
            continue
        
        if last != nums[i] and (len(arr) == 0 or arr[-1] <= nums[i]) :
            
            arr.append(nums[i])
            last = nums[i]
            dfs(depth + 1)
        
            
            arr.pop()
            for j in range(i+1,N):
                visited[j] = False
            
dfs(0)
            
            