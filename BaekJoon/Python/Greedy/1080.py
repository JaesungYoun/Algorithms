import sys

N,M = map(int,sys.stdin.readline().split())

A = []
B = []
for _ in range(N):
    A.append(list(map(int,sys.stdin.readline().rstrip())))
for _ in range(N):
    B.append(list(map(int,sys.stdin.readline().rstrip())))
    

def reverse(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            A[i][j] = 1 - A[i][j]

count = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            reverse(i,j)
            count += 1

for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            print(-1)
            exit(0)        
else:
    print(count)

