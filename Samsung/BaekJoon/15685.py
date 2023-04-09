N = int(input())


info = []
for _ in range(N):
    info.append(list(map(int,input().split())))

mat = [[0]*101 for _ in range(101)]


# 동,북,서,남
dx = [1,0,-1,0]
dy = [0,-1,0,1]


for x,y,d,g in info:
    mat[x][y] = 1
    
    curve = [d] 
    
    # 커브 방향 리스트 만들기
    for i in range(g):
        for j in range(len(curve)-1,-1,-1): # index는 length보다 1 작으므로 시작을 length -1 부터
            curve.append((curve[j]+1)%4)

    # 드래곤 커브 그리기
    for i in range(len(curve)):
        x += dx[curve[i]]
        y += dy[curve[i]]
        if 0<=x<101 and 0<=y<101:
            mat[x][y] = 1


cnt = 0
for i in range(100):
    for j in range(100):
        # 정사각형 꼭짓점 모두 검사
        if mat[i][j] == 1 and mat[i+1][j] == 1 and mat[i][j+1] and mat[i+1][j+1] == 1:
            cnt += 1  
print(cnt)
    


