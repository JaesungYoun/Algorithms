
T = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]


for tc in range(1,T+1):
    N = int(input())

    snail = [[0 for _ in range(N)] for _ in range(N)]

    x,y = 0,0
    dist = 0

    for n in range(1,N*N+1):
        snail[x][y] = n

        nx = x + dx[dist]
        ny = y + dy[dist]

        if not (0<=nx<N and 0<=ny<N) or snail[nx][ny] != 0:
            dist = (dist+1) % 4

            nx = x + dx[dist]
            ny = y + dy[dist]
        x,y= nx,ny

    for row in snail:
        print(*row)

    print()