N,M = map(int,input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))

    # 북,동,남,서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
direction = [ # cctv 번호에 따른 회전 방향
        [],
        [[0], [1], [2], [3]], # 1번 CCTV
        [[0, 2], [1, 3]], # 2번 CCTV
        [[0, 1], [1, 2], [2, 3], [3, 0]], # 3번 CCTV
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], # 4번 CCTV
        [[0, 1, 2, 3]] # 5번 CCTV
    ]

def dfs(depth,arr): # 모든 경우의 수 탐색
    global min_val
    
    if depth == len(cctv):
        min_val = min(min_val,count(arr))
        return
    
    temp = [i[:] for i in arr]
    
    x,y,cctv_num = cctv[depth] 
    for i in direction[cctv_num]: # cctv num에 따른 모든 방향 경우의 수 탐색
        check(x,y,i,temp)
        dfs(depth+1,temp)
        temp = [i[:] for i in arr]

def check(x,y,dir,arr):
    for d in dir:
        nx = x
        ny = y 
        while True:
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < N and 0<= ny < M and arr[nx][ny] != 6:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 2
            else:
                break
        
def count(mat):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 0:
                cnt += 1

    return cnt  

min_val = 1e9
cctv = []
for i in range(N):
    for j in range(M):
        if 1<= mat[i][j] <= 5:
            cctv.append([i,j,mat[i][j]]) # 좌표, cctv 번호
dfs(0,mat)
print(min_val)