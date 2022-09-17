import sys

N = int(sys.stdin.readline())


dp = [0] * 1001
dp[1] = 0
dp[2] = 1
dp[3] = 0
dp[4] = 1

for i in range(5, N + 1):
    if not dp[i - 1] :
        dp[i] = 1
    if not dp[i - 3]:
        dp[i] = 1
    if not dp[i - 4]:
        dp[i] = 1 

if dp[N]:
    print("SK")
else:
    print("CY")