from collections import deque

N, M = map(int, input().split())
mat = []

for _ in range(N):
    mat.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, color):
    visited[x][y] = 1
    queue = deque([(x, y)])
    rainbow = []
    normal = [(x, y)]
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if mat[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    rainbow.append((nx, ny))
                elif mat[nx][ny] == color:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    normal.append((nx, ny))

    for x, y in rainbow:
        visited[x][y] = 0

    return [len(rainbow) + len(normal), len(rainbow), normal + rainbow]


def remove_block(group):
    global answer
    answer += group[0] ** 2

    for x, y in group[2]:
        mat[x][y] = -2  # 블록 제거


def gravity():
    for i in range(N - 2, -1, -1):  # 가장 아래행의 윗 행부터 이동 시작
        for j in range(N):
            if mat[i][j] != -1:
                now = i  # 현재 행

                while now + 1 < N and mat[now + 1][j] == -2:
                    mat[now + 1][j] = mat[now][j]  # 아래로 이동
                    mat[now][j] = -2  # 이동을 했으므로 빈 칸으로 만들어줌
                    now += 1  # 맨 윗칸의 경우 계속 이동해야 하므로 now에 1을 더해줌


def turn_left():
    global mat
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = mat[j][N - i - 1]
    mat = temp


answer = 0  # 점수

while 1:
    visited = [[0 for _ in range(N)] for _ in range(N)]

    groups = []

    for i in range(N):
        for j in range(N):
            if mat[i][j] > 0 and visited[i][j] == 0:
                group = bfs(i, j, mat[i][j])

                if group[0] >= 2:
                    groups.append(group)

    groups.sort(reverse=True)
    print(groups)
    if not groups:
        break

    remove_block(groups[0])
    gravity()
    turn_left()
    gravity()

print(answer)
