N,M = map(int,input().split())

nums = list(map(int,input().split()))
nums.sort()
arr = []
visited = [False] * (N+1)
def dfs(depth):
    if depth == M:
        print(*arr)
        return

    
    for i in range(N):
        if visited[i]:
            continue
        arr.append(nums[i])
        visited[i] = True
        dfs(depth + 1)
        arr.pop()

        visited[i] = False

dfs(0)


    