import sys

T = int(sys.stdin.readline())
def solve(arr):
    global level
    
    
    for i in range(len(arr)+1):
        level = min(level,abs(arr[i%N] - arr[(i+1)%N]))
    
    return 
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))
    
    arr.sort()
    level = 0
    
    for i in range(2,N):
        level = max(level,abs(arr[i]-arr[i-2]))
    print(level)

