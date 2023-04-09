from collections import deque

N, M, K = map(int, input().split())

mat = [[deque() for _ in range(N)] for _ in range(N)]
fireball = deque()

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append((r - 1, c - 1))
    mat[r - 1][c - 1].append([m, s, d])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(K):
    # 파이어볼 이동
    for j in range(len(fireball)):
        x, y = fireball.pop()
        m, s, d = mat[x][y].popleft()
        nx = (s * dx[d] + x) % N
        ny = (s * dy[d] + y) % N
        mat[nx][ny].append([m, s, d])
    # 2개이상인지 체크
    for r in range(N):
        for c in range(N):
            # 2개 이상인 경우 -> 4개의 파이어볼로 쪼개기
            if len(mat[r][c]) > 1:
                sum_m, sum_s, odd_d, even_d, cnt = 0, 0, 0, 0, 0
                while mat[r][c]:
                    m, s, d = mat[r][c].pop()
                    sum_m += m
                    sum_s += s
                    cnt += 1
                    if d % 2 == 0:
                        even_d += 1
                    else:
                        odd_d += 1
                sum_m //= 5
                if sum_m == 0:
                    continue
                sum_s //= cnt
                if even_d == cnt or odd_d == cnt:
                    dir = [0, 2, 4, 6]
                else:
                    dir = [1, 3, 5, 7]

                for d in range(4):
                    fireball.append([r, c])
                    mat[r][c].append([sum_m, sum_s, dir[d]])
            elif len(mat[r][c]) == 1:
                fireball.append([r, c])

answer = 0
for i in range(N):
    for j in range(N):
        answer += sum(arr[0] for arr in mat[i][j])

print(answer)