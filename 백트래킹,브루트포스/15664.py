import sys

N,M = map(int,sys.stdin.readline().split())

nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
arr = []
visited = [False] * N
def dfs(idx):
    if len(arr) == M:
        print(*arr)
        return
    
    last = 0
    for i in range(idx,N): # 비내림차순으로 i+1 부터 탐색
        if visited[i]:
            continue
        
        if last != nums[i]:
            arr.append(nums[i])
            last = nums[i]
            visited[i] = True
            dfs(i + 1)
            arr.pop()
            visited[i] = False
                
dfs(0)
