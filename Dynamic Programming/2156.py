import sys

n = int(sys.stdin.readline())

podo = [0] * 10001

dp = [0] * 10001


for i in range(1,n+1):
    podo[i] = int(sys.stdin.readline())

dp[1] = podo[1]
dp[2] = podo[1] + podo[2]
dp[3] = max(podo[2] + podo[3], podo[1] + podo[3], dp[2])
for i in range(4,n+1):
    dp[i] = max(dp[i-3] + podo[i-1] + podo[i],dp[i-1],dp[i-2] + podo[i])

print(dp[n])

