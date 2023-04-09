t = int(input())
f = int(input())
for _ in range(t):
    arr = []
    for i in range(f):
        arr.append(list(map(int,input().split())))
    n = len(arr)
    dp = [[0] * n for i in range(n)]
    print(dp)
    for i in range(len(arr)):
        idx = arr[i][0]
        val = arr[i][1]

        dp[i][idx] = val
    
    for i in range(1,len(dp)):
        for j in range(i+1):
            if dp[i][j] == 0:
                if j == 0:
                    dp[i][j] = dp[i-1][j] - dp[i][j+1]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] - dp[i][j-1]
                else:
                    if dp[i][j-1] != 0:
                        dp[i][j] = dp[i-1][j-1] - dp[i][j-1]
                    elif dp[i][j+1] != 0:
                        dp[i][j] = dp[i-1][j] - dp[i][j+1]
    
    

    print(dp)