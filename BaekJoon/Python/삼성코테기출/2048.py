
from copy import deepcopy

N = int(input())

mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))

def move(mat,d):
    if d == 0: # 서쪽으로 
        for i in range(N):
            top = 0
            for j in range(1,N):
                if mat[i][j]:
                    temp = mat[i][j]
                    mat[i][j] = 0 
                    if mat[i][top] == 0:
                        mat[i][top] = temp
                    elif mat[i][top] == temp:
                        mat[i][top] = temp * 2
                        top += 1
                    else:
                        top += 1
                        mat[i][top] = temp
    
    elif d == 1: # 동쪽
        for i in range(N):
            top = N - 1
            for j in range(N-2,-1,-1):
                if mat[i][j]:
                    temp = mat[i][j]
                    mat[i][j] = 0
                    if mat[i][top] == 0:
                        mat[i][top] = temp
                    elif mat[i][top] == temp:
                        mat[i][top] = temp * 2
                        top -= 1
                    else:
                        top -= 1
                        mat[i][top] = temp

    elif d == 2: # 북쪽
        for j in range(N):
            top = 0
            for i in range(1,N):
                if mat[i][j]:
                    temp = mat[i][j]
                    mat[i][j] = 0
                    if mat[top][j] == 0:
                        mat[top][j] = temp
                    elif mat[top][j] == temp:
                        mat[top][j] = temp * 2
                        top += 1
                    else:
                        top += 1
                        mat[top][j] = temp
    else:
        for j in range(N):
            top = N - 1
            for i in range(N - 2, -1, -1):
                if mat[i][j]:
                    tmp = mat[i][j]
                    mat[i][j] = 0
                    if mat[top][j] == 0:
                        mat[top][j] = tmp
                    elif mat[top][j] == tmp:
                        mat[top][j] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        mat[top][j] = tmp
    return mat


        

def dfs(mat,count):
    global answer 
    if count == 5:
        for i in range(N):
            for j in range(N):
                answer = max(answer, mat[i][j])
        return

    
    for i in range(4):
        new_mat = move([j[:] for j in mat],i)
        dfs(new_mat, count + 1)

answer = 0
dfs(mat,0)
print(answer)