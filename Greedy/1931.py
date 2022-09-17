import sys

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))



arr = sorted(arr, key = lambda x: (x[1],x[0]))
cnt = 1

end = arr[0][1]

for i in range(1,N):
    if arr[i][0] >= end:
        cnt += 1
        end = arr[i][1]
    
print(cnt)