import sys

X,Y = map(int,sys.stdin.readline().split())


Z = (Y*100) // X

start = 0
end = 1000000000

if Z >= 99:
    print(-1)
else:
    while start <= end:
        
        mid = (start + end) // 2
        new_X = X + mid
        new_Y = Y + mid
        if new_Y*100 // new_X > Z:
            end = mid - 1
        else:
            start = mid + 1
        
    print(end + 1)
