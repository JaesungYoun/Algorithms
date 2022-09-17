import sys

T = int(sys.stdin.readline())

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4


for i in range(4,len(dp)):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(T):
    n = int(sys.stdin.readline())
    print(dp[n])