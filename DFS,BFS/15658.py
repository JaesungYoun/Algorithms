import sys

N = int(sys.stdin.readline())

nums = list(map(int,sys.stdin.readline().split()))

add,sub,mul,div = map(int,sys.stdin.readline().split())

maximum = -1e9
minimum = 1e9
total = nums[0]
def dfs(depth,total,add,sub,mul,div):
    global maximum,minimum
    if depth == N:
        maximum = max(total,maximum)
        minimum = min(total,minimum)
        return
        
    if add > 0:
        dfs(depth + 1,total + nums[depth], add - 1,sub,mul,div)
    if sub > 0:
        dfs(depth + 1,total - nums[depth], add ,sub-1,mul,div)
    if mul > 0:   
        dfs(depth + 1,total * nums[depth], add,sub,mul-1,div)
    if div > 0:
        if total < 0:
            dfs(depth + 1,-(abs(total) // nums[depth]), add,sub,mul,div-1)
        else:
            dfs(depth + 1,total // nums[depth], add,sub,mul,div-1)

dfs(1,total,add,sub,mul,div)
print(maximum)
print(minimum)