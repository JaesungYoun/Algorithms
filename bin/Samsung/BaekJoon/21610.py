N, M = map(int, input().split())

mat = []
for i in range(N):
    mat.append(list(map(int, input().split())))

move_info = []
for _ in range(M):
    d, s = map(int, input().split())
    move_info.append([d - 1, s])

# 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

cloud = [[0 for _ in range(N)] for _ in range(N)]
cloud[N - 1][0] = -3
cloud[N - 1][1] = -3
cloud[N - 2][0] = -3
cloud[N - 2][1] = -3

for i in range(M):  # M 번 이동
    d = move_info[i][0]
    s = move_info[i][1]

    temp = []
    for x in range(N):
        for y in range(N):
            if cloud[x][y] == -3:
                nx = (x + s * dx[d]) % N
                ny = (y + s * dy[d]) % N

                mat[nx][ny] += 1  # 2. 비가 내려서 바구니에 저장된 물이 1 증가
                # 물복사버그 마법

                temp.append((nx, ny))
                cloud[x][y] = 0  # 구름이 사라짐


    for x, y in temp:
        cnt = 0
        for k in range(1, 8, 2):
            a = x + dx[k]
            b = y + dy[k]
            if 0 <= a < N and 0 <= b < N:
                if mat[a][b] > 0:
                    cnt += 1
        mat[x][y] += cnt

    for x in range(N):
        for y in range(N):
            if mat[x][y] >= 2 and (x, y) not in temp:
                cloud[x][y] = -3  # 구름 생성
                mat[x][y] -= 2


result = 0
for i in range(N):
    for j in range(N):
        result += mat[i][j]

print(result)