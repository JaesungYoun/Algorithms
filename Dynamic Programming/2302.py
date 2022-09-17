import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

vip = []

for _ in range(M):
    vip.append(int(sys.stdin.readline()))


dp = [0] * (N+2)


dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3,N+1):
    dp[i] = dp[i-1] + dp[i-2]
    
cnt = 1
if M > 0:
    temp = 0
    for i in range(M):
        cnt *= dp[vip[i]-1-temp]
        temp = vip[i]
        
    cnt *= dp[N-temp]
else:
    cnt = dp[N]


print(cnt)        
        