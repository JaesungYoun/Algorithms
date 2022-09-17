import sys

k = int(sys.stdin.readline())

nums = list(map(int,sys.stdin.readline().split()))
tree = [[] for _ in range(k)]
idx = 0
def inorder(depth):
    global tree,idx
    if depth == k:
        return

    
    
    inorder(depth+1) # left
    tree[depth].append(nums[idx]) # root
    idx += 1
    inorder(depth+1) # right
    
    
inorder(0)
for i in tree:
    print(*i)