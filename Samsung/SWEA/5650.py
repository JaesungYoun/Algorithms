from collections import defaultdict
import itertools


# 방향 전환
change = [
    # 상 하 좌 우일 때 변화
    [1,3,0,2], # 1번 삼각형
    [3,0,1,2],# 2번 삼각형
    [2,0,3,1], # 3번 삼각형
    [1,2,3,0], # 4번 삼각형
    [1,0,3,2], # 5번 정사각형
]
# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def moving(x,y,d): # 핀볼이 움직이는 함수

    score = 0
    start_x,start_y = x,y # 핀볼 시작 위치
    while 1: # 핀볼 이동
        x += dx[d]
        y += dy[d]
        if not (0<=x<N and 0<=y<N): # 벽에 부딪힌 경우
            if d in [0,2]:
                d += 1
            else:
                d -= 1
            score += 1 # 점수 더해줌
        else:
            if (x,y) == (start_x,start_y) or mat[x][y] == -1: # 블랙홀이거나 시작위치이면
                return score
            elif 1 <= mat[x][y] <= 5:
                d = change[mat[x][y]-1][d]
                score += 1
            elif 6 <= mat[x][y] <= 10:
                x,y = wormhole[(x,y)]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    w = [0] * 11
    wormhole = defaultdict(tuple)# 같은 번호의 웜홀 저장
    max_score = - 1

    N = int(input())
    mat = []
    for _ in range(N):
        mat.append(list(map(int,input().split())))

    for x in range(N):
        for y in range(N):
            if 6<=mat[x][y] <=10:
                num = mat[x][y]
                if w[num] == 0: # 쌍 중에 먼저 들어오면
                    w[num] = (x,y)
                else:
                    wormhole[w[num]] = (x,y)
                    wormhole[(x,y)] = w[num]

    a = [i for i in range(N)]
    '''
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 0:
                for d in range(4):
                    max_score = max(max_score, moving(i, j, d))
    '''
    pp = list(itertools.product(a,repeat =2))

    for p in pp:
        for d in range(4):
            if mat[p[0]][p[1]] == 0:
                max_score = max(max_score,moving(p[0],p[1],d))



    print("#{} {}".format(test_case,max_score))

