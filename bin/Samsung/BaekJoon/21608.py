from collections import defaultdict
N = int(input())

student = defaultdict(list)
for _ in range(N**2):
    arr = list(map(int,input().split()))
    student[arr[0]] = arr[1:]


mat = [[0 for _ in range(N)] for _ in range(N)] # 교실

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def count_like(x,y,arr):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if mat[nx][ny] in arr:
                cnt += 1
    return cnt
def count_blank(x,y): # 인접한 빈칸 세는 함수
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N:
            if mat[nx][ny] == 0:
                cnt += 1

    return cnt

for k,v in student.items(): # 학생 수 만큼 반복
    max_friend = -1 # 좋아하는 인접한 친구의 수
    max_val = -1 # 2번 조건을 위한 변수
    # 값이 0인경우도 생각해야하므로 -1로 셋팅!

    pos_x = -1 # 자리
    pos_y = -1
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 0: # 비어있는 칸이면
                if max_friend <= count_like(i,j,v):
                    if max_friend == count_like(i,j,v):
                        if max_val < count_blank(i, j):
                            max_val = count_blank(i, j)
                            pos_x = i
                            pos_y = j

                    else:
                        max_friend = count_like(i,j,v)
                        max_val = count_blank(i, j)
                        pos_x = i
                        pos_y = j
    mat[pos_x][pos_y] = k

answer = 0
for i in range(N):
    for j in range(N):
        if count_like(i,j,student[mat[i][j]]) > 0:
            answer += 10**(count_like(i,j,student[mat[i][j]])-1)



print(answer)