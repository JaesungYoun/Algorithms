import sys

N = int(sys.stdin.readline())
hp_consume = [0] + list(map(int,sys.stdin.readline().split()))
get_joy = [0] + list(map(int,sys.stdin.readline().split()))

dp = [[0] * 101 for _ in range(N+1)]


        
for i in range(1,N+1):
    for j in range(1,101):
        if hp_consume[i] <= j:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-hp_consume[i]] +get_joy[i])
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[N][99])         
