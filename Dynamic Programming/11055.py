import sys
sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())

seq = list(map(int,sys.stdin.readline().rstrip().split()))


dp = seq[:]


for i in range(1,N):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i],dp[j]+seq[i])
            

print(max(dp))

    
    