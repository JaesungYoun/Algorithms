import sys
n,k = map(int,sys.stdin.readline().split())

values = []
for _ in range(n):
    values.append(int(sys.stdin.readline()))


dp =[0] * (k+1)
dp[0] = 1

for v in values:
    for i in range(v,k+1):
        if i - v >= 0:
            dp[i] += dp[i-v]

print(dp[k])