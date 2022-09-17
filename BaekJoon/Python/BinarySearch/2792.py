import sys

N,M = map(int,sys.stdin.readline().split())
color = []
for i in range(M):
    color.append(int(sys.stdin.readline()))
    

start = 1
end = max(color)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in color:
        if i % mid == 0:
            total += i // mid
        else:
            total += (i // mid) + 1
    
    if total > N:
        start = mid + 1
    else:
        end = mid - 1
    
print(start)