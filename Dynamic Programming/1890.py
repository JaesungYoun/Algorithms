import sys

N = int(sys.stdin.readline())

nums = []
dp = [[0] * N for _ in range(N)]
for _ in range(N):
    nums.append(list(map(int,sys.stdin.readline().split())))

dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            print(dp[i][j])
            break
        
        if j + nums[i][j] < N:
            dp[i][j+nums[i][j]] += dp[i][j]
        if i + nums[i][j] < N:
            dp[i+nums[i][j]][j] += dp[i][j]


            