import sys

N = int(sys.stdin.readline())

egg = []

for _ in range(N):
    egg.append(list(map(int,sys.stdin.readline().split())))    

max_cnt = 0
def dfs(depth):
    global max_cnt,egg
    if depth == N:
        cnt = 0
        for i in range(len(egg)):
            if egg[i][0] <= 0:
               cnt += 1
        max_cnt = max(max_cnt,cnt)
        return

    if egg[depth][0] > 0:
        for i in range(N):
            flag = False
            if egg[i][0] > 0 and i != depth:
                flag = True
                egg[depth][0] -= egg[i][1]
                egg[i][0] -= egg[depth][1]
                dfs(depth + 1)
                egg[depth][0] += egg[i][1]
                egg[i][0] += egg[depth][1]
                
        if not flag:
            dfs(depth + 1)        
    else:
        dfs(depth + 1)
        
dfs(0)
print(max_cnt)
    