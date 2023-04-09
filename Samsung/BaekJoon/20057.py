n = int(input())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

board = [list(map(int, input().split())) for _ in range(n)]
result = 0 # 격자 밖으로 나간 모래의 양
now_x, now_y = n // 2, n // 2 # 토네이도 시작위치

# 각 방향으로 이동했을 때의 각 좌표의 비율
left = [[0,0,2,0,0],[0,10,7,1,0],[5,-1,0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
right = [[0,0,2,0,0],[0,1,7,10,0],[0,0,0,-1,5],[0,1,7,10,0],[0,0,2,0,0]]
up = [[0,0,5,0,0],[0,10,-1,10,0],[2,7,0,7,2],[0,1,0,1,0],[0,0,0,0,0]]
down = [[0,0,0,0,0],[0,1,0,1,0],[2,7,0,7,2],[0,10,-1,10,0],[0,0,5,0,0]]

def move(cnt,dx,dy,direction):
    global result,now_x,now_y
    for i in range(cnt+1): # 이동 횟수
        now_x,now_y = now_x + dx, now_y + dy # 토네이도 이동 ( 토네이도 위치) y 위치
        if now_x <0 or now_y <0: # 토네이도가 0,0까지 도달 후 종료
            break

        a_x,a_y= -1,-1
        a,b = now_x-2,now_y-2 # 토네이도 위치에서 2만큼씩 뱬거니까
        spread = 0
        for i in range(5):
            for j in range(5):
                # left,right,up,down
                if direction[i][j] != 0 and direction[i][j] != -1: # a위치이거나, 비율이 적혀있는 위칭ㄴ 경우
                    if 0<=a+i<n and 0<=b+j<n: # 범위 안일 때
                        board[a+i][b+j] += board[now_x][now_y] * direction[i][j]//100 # 비율이 적혀있는 자리
                    else:
                        result += board[now_x][now_y] * direction[i][j]//100
                    spread += board[now_x][now_y] * direction[i][j]//100 # 흩어진 모래의 양을 계산
                elif direction[i][j] == -1: # a 위치이면
                    a_x,a_y = i,j # a 좌표를 저장

        if 0<=a+a_x<n and 0<=b+a_y<n: # a좌표가 범위 안에 있으면
            board[a+a_x][b+a_y] += board[now_x][now_y] - spread # 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의양을 더해줌
        else: # 범위 밖이면 정답에 모래양을 더해줌
            result += board[now_x][now_y] - spread
        board[now_x][now_y] = 0


# 토네이도 이동 규칙
for i in range(n):
    if i % 2 == 0: # 왼쪽,아래쪽인 경우
        move(i,0,-1,left)
        move(i,1,0,down)
    elif i % 2 == 1: # 오른쪽, 위쪽으로 이동인 경우
        move(i,0,1,right)
        move(i,-1,0,up)

print(result)