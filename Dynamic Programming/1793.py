import sys


dp = [0] * 251
dp[0] = 1
dp[1] = 1
dp[2] = 3
for i in range(3,251):
        dp[i] = dp[i-2] * 2 + dp[i-1] 


while 1:
    try:
        n = int(sys.stdin.readline().rstrip())
        print(dp[n])
    except:
        break
    