import sys

N = int(sys.stdin.readline())


sum = 0 
for i in range(1,N+1):
    sum += (N//i)*i

print(sum)