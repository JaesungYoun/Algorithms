import sys

N = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))

dp = [1] * (N+1)

for i in range(len(A)):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i],dp[j]+1)
    print(dp)
print(max(dp))