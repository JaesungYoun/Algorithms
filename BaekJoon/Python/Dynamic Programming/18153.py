n = int(input())

arr = list(map(int,input().split()))
# 가장 긴 감소하는 부분수열을 찾는 문제이다(LIS의 반대)
arr.reverse()

dp = [1] * n

for i in range(1,n):
    for j in range(0,i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j]+1,dp[i])


# 열외해야하는 병사의 최소 수
print(n-max(dp))