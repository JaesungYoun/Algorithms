import sys


N,S,M = map(int,sys.stdin.readline().split())

v = list(map(int,sys.stdin.readline().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)] # 2차원 배열(각 곡마다 볼륨을 저장)

dp[0][S] = 1

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == 1:
            if j - v[i] >= 0:
                dp[i+1][j-v[i]] = 1
                
            if j + v[i] <= M:
                dp[i+1][j+v[i]] = 1
                
            
# 반복문을 통해 마지막 곡에 최대 볼륨을 찾는다.
for k in range(M, -1, -1):
    if dp[N][k] == 1:
        print(k)
        exit()

# 마지막 곡에 볼륨이 없다면 -1 출력
print(-1)