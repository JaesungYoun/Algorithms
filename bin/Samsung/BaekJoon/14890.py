N,L= map(int,input().split())

mat = []

for i in range(N):
    mat.append(list(map(int,input().split())))


def check(road):
    for i in range(1,N):
        if abs(road[i] - road[i-1]) > 1 :
            return False
        if road[i] < road[i-1]:
            for j in range(L):
                if i + j >= N or road[i] != road[i+j] or slope[i+j]:
                    return False
                if road[i] == road[i+j]: # 경사로 놓기 (뒤에서 다른 높이가 나와도 위 if 문 
                    slope[i+j] = True   

        elif road[i] > road[i-1]:
            for j in range(L):
                if i - j - 1 < 0 or road[i-1] != road[i-j-1] or slope[i-j-1]:
                    return False
                if road[i-j-1] == road[i-1]:
                    slope[i-j-1] = True
    return True

cnt = 0

for i in mat:
    slope = [False] * (N+1)
    if check(i):
        cnt += 1

for j in range(N):
    slope = [False] * N  
    if check([mat[i][j] for i in range(N)]):
        cnt += 1    
print(cnt)

