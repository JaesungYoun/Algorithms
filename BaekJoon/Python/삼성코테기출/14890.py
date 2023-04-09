import sys

N,L = map(int,sys.stdin.readline().split())

mat = []
for _ in range(N):
    mat.append(list(map(int,sys.stdin.readline().split())))

def check(road):
    for i in range(N-1):
        if abs(road[i] - road[i+1]) > 1:
            return False
        if road[i] > road[i+1]:
            for j in range(L):
                if i + j + 1>= N or road[i+1] != road[i+j+1] or slope[i+j+1]:
                    return False
                if road[i+1] == road[i+j+1]: # 경사로 놓기 (뒤에서 다른 높이가 나와도 위 if 문 
                    slope[i+j+1] = True           #      에서 걸러진다.)
        elif road[i+1] > road[i]:            
            for j in range(L):
                if i-j < 0 or road[i] != road[i-j] or slope[i-j]:
                    return False
                if road[i] == road[i-j]:
                    slope[i-j] = True 
    return True


cnt = 0
for i in range(N):
    slope = [False] * N
    if check(mat[i]):
        cnt += 1
for j in range(N):
    slope = [False] * N  
    if check([mat[i][j] for i in range(N)]):
        cnt += 1      
print(cnt)

