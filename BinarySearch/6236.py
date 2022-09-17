import sys

N,M = map(int,sys.stdin.readline().split())

value = []

for _ in range(N):
    value.append(int(sys.stdin.readline()))


K = 0
start = min(value)
end = sum(value)
while start<=end:
    mid = (start + end) // 2 
    draw = mid
    cnt = 1
    
    for i in range(N):
        if draw < value[i]:
            draw = mid
            cnt += 1
        draw -= value[i]
    
    if cnt > M or mid < max(value):
        start = mid + 1
    else:
        end = mid - 1
        K = mid
        
print(K)