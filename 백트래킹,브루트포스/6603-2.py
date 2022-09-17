import sys


def dfs(depth,idx):
    if depth == 6:
        print(*c)
        return

    for i in range(idx,k):
        c.append(S[i])
        dfs(depth+1,i+1)
        c.pop()
        



while 1:
    S = list(map(int,sys.stdin.readline().strip().split()))
    k = S[0]
    S = S[1:]
    if k == 0 :
        break
    c = []
    dfs(0,0)
    print()
    
    