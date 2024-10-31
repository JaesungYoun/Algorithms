N,M = map(int,input().split())

output = []

arr = list(map(int,input().split()))
arr.sort()
visited = [0 for _ in range(N)]
def dfs(depth):
    if depth == M:
        print(*output)
        return

    for i in range(N):
        if visited[i]:
            continue
        output.append(arr[i])
        visited[i] = 1
        dfs(depth + 1)
        output.pop()
        visited[i] = 0

dfs(0)

