import sys
from collections import defaultdict

T = int(sys.stdin.readline())

dic = defaultdict(list)


def dfs(graph,start,visited):
    visited[start] = True
    
    for i in graph[start]:
        if visited[i] == False:
            dfs(graph,i,visited)


for i in range(T):
    cycle = 0
    
    N = int(sys.stdin.readline())
    arr = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    nums = list(map(int,sys.stdin.readline().split()))
    
    for j in range(1,len(nums)+1):
        if nums[j-1] == j:
            cycle += 1
        else:
            arr[j].append(nums[j-1])
            arr[nums[j-1]].append(j)
    
    
    for j in range(1,N+1):
        if not visited[j] and nums[j-1] != j:
            dfs(arr,j,visited)
            cycle += 1
        
    print(cycle)