import sys

M,N = map(int,sys.stdin.readline().split())

l = list(map(int,sys.stdin.readline().split()))

start = 1
end = max(l)
result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    if mid == 0:
        break
    
    for i in l:
        total += i // mid
        
    
    if total >= M:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)