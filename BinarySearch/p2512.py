import sys

N = int(sys.stdin.readline())

req = list(map(int,sys.stdin.readline().split()))

budget = int(sys.stdin.readline())

if sum(req) <= budget:
    print(max(req))
else:
    start = 0
    end = max(req)
    
    while start <= end:
        mid = (start + end) // 2
        a = 0
        
        for i in range(len(req)):
            if req[i] >= mid:
                a += mid
            else:
                a += req[i]
        
        if a > budget:
            end = mid - 1
        else:
            start = mid + 1
    print(end)
    
    