import sys


T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    dp = [1 for i in range(10)] # 한자리수 1로 초기화

    for i in range(n-1): 
        for j in range(10): # 앞자리가 0으로 시작하는 경우 
            dp[j] = sum(dp[j:]) # 뒷자리의 경우의 수 다 더해줌
    print(sum(dp))
    
# 1 1 1 1 1 1 1 1 1 1
# 10 9 8 7 6 5 4 3 2 1  앞자리가 0으로 시작하는 경우 10개, 앞자리가 1로 시작하는 경우 9개 .....