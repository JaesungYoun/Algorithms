import sys


T = int(sys.stdin.readline())

for _ in range(T):
    mat = []
    
    n = int(sys.stdin.readline())
    
    for _ in range(2):
        mat.append(list(map(int,sys.stdin.readline().split())))
    
    if n == 1:
        print(max(mat[0][0], mat[1][0]))
    else:
        mat[0][1] += mat[1][0]
        mat[1][1] += mat[0][0]
    
        for i in range(2,n):
            mat[0][i] += max(mat[1][i-1], mat[1][i-2])
            mat[1][i] += max(mat[0][i-1], mat[0][i-2])
        print(max(mat[0][n-1],mat[1][n-1]))