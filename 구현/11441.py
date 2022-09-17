import sys

N = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())


hab = 0 
accu_sum = [0]
for i in range(len(A)):
    hab += A[i]
    accu_sum.append(hab)

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    print(accu_sum[j] - accu_sum[i-1])
    
    