import sys

N = int(sys.stdin.readline())

nums = list(map(int,sys.stdin.readline().split()))

oper = list(map(int,sys.stdin.readline().split()))

max_val = -1e9
min_val = 1e9

def dfs(depth,total,add,sub,mul,div):
    global oper,max_val,min_val
    
    if depth == N:
        max_val = max(max_val,total)
        min_val = min(min_val,total)
        return
    
    if add > 0:
        dfs(depth + 1, total + nums[depth],add-1,sub,mul,div)
    if sub > 0:
        dfs(depth + 1, total - nums[depth],add,sub-1,mul,div)
    if mul > 0:
        dfs(depth + 1, total * nums[depth],add,sub,mul-1,div)
    if div > 0:
        if total < 0:
            dfs(depth+1, -(abs(total) // nums[depth]),add,sub,mul,div-1)
        else:
            dfs(depth+1, total // nums[depth],add,sub,mul,div-1)
        
dfs(1,nums[0],oper[0],oper[1],oper[2],oper[3])

print(max_val)
print(min_val)