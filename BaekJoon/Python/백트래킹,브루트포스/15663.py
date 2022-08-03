import sys

N,M = map(int,sys.stdin.readline().split())

nums = list(map(int,sys.stdin.readline().split()))
nums.sort()

arr = []

visited = [False] * (N)
def dfs(depth):
    if depth == M:
        print(*arr)
        return
    last = 0
    for i in range(N):
        if visited[i] == True:
            continue
        if last != nums[i]:
            arr.append(nums[i])
            
            visited[i] = True
            last = nums[i]
            dfs(depth + 1)
            arr.pop()
            visited[i] = False
        
dfs(0)
