import sys

n,k = map(int,sys.stdin.readline().split())

coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

dp = [10001] * (k+1)
dp[0] = 0


for c in coins:
    for i in range(1,k+1):
        if i - c >= 0:
            dp[i] = min(dp[i],dp[i-c] + 1)
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])

