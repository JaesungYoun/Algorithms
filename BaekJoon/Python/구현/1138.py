import sys

N = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

result = [0] * N

for i in range(1,N+1):
    h = a[i-1]
    cnt = 0
    for j in range(N):
        if cnt == h and result[j]==0:
            result[j] = i
            break
        elif result[j] == 0:
            cnt += 1
            
print(*result)