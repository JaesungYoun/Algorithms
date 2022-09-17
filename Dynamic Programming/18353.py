from re import S


import sys

N = int(sys.stdin.readline())

ab = list(map(int,sys.stdin.readline().split()))


dp = [1] * N

for i in range(len(ab)):
    for j in range(i):
        if ab[j] > ab[i]:
            dp[i] = max(dp[i],dp[j]+1)
            

print(N - max(dp))
        
    