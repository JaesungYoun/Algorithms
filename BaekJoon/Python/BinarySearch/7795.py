import sys

T = int(sys.stdin.readline())


for i in range(T):
    N,M = map(int,sys.stdin.readline().split())
    A = sorted(list(map(int,sys.stdin.readline().split())))
    B = sorted(list(map(int,sys.stdin.readline().split())))
    
    result = 0
    for i in A:
        start = 0
        end = len(B) - 1
        cnt = -1
        while start <= end:
            mid = (start + end) // 2
            if B[mid] < i:
                cnt = mid
                start = mid + 1
            else:
                end = mid - 1
        
        result += (cnt + 1)
    print(result)
