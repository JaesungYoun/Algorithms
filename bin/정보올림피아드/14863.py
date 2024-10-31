import sys
input=sys.stdin.readline
N,K=map(int,input().split())
DP=[[-100 for _ in range(K+1)] for _ in range(N+1)]
DP[0][0]=0
for i in range(1,N+1):
    w, w_money, b, b_money=map(int,input().split())
    for j in range(K+1): 
        if DP[i-1][j]!=-100 :
            if j+w<=K: DP[i][j+w]=max(DP[i][j+w],DP[i-1][j]+w_money)
            if j+b<=K: DP[i][j+b]=max(DP[i][j+b],DP[i-1][j]+b_money)


ans=0
for a in range(K+1):
    if DP[N][a]!=-100 :
        ans=max(ans,DP[N][a])
print(ans)


# DFS 풀이 (완전탐색)
''' 
n,k = map(int,input().split())
dobo = []
bicy = []
for _ in range(n):
    a,b,c,d = map(int,input().split())
    dobo.append([a,b])
    bicy.append([c,d])


result = 0
visited = [0] * (n+1)
def dfs(cnt,time,total):
    global result

    if cnt == n:
        if time <= k:
            result = max(result,total)
            return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(cnt+1,time+dobo[i][0],total+dobo[i][1])
        dfs(cnt+1,time+bicy[i][0],total+bicy[i][1])

        visited[i] = 0
dfs(0,0,0)
print(result)

'''