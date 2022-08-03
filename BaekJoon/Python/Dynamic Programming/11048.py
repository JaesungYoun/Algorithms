import sys

N,M = map(int,sys.stdin.readline().split())

candies = []

dp = [[0]*(M+1) for i in range(N+1)]

for i in range(N):
    candies.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = candies[i-1][j-1] + max(dp[i-1][j], dp[i][j-1],dp[i-1][j-1])
        
print(dp[N][M])