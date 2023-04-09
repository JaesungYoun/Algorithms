N,M,H= map(int,input().split())

board = [[0] * N for _ in range(H)]
for _ in range(M):
    a,b = map(int,input().split())
    board[a-1][b-1] = 1


if M == 0:
    print(0)
    exit(0)

def check():
    for i in range(N):
        now = i
        for j in range(H):
            if board[j][now] == 1:
                now += 1
            elif now > 0 and board[j][now-1] == 1:
                now -= 1
        if i != now:
            return False
    return True

def dfs(cnt,x,y):
    global min_val

    if check(): # 가로선을 하나씩 추가할 때마다 체크해줘야함
        min_val = min(min_val,cnt)
        return
    if cnt == 3:
        return


    for i in range(x,H):
        if i == x: # 행이 그대로이면
            now = y # 탐색하던 j + 2 세로줄부터 탐색
        else: # 재귀타고 갔는데, 행이 바뀌면
            now = 0 # 처음 세로줄부터 다시 탐색
        for j in range(now,N-1): # 세로줄 탐색
            if board[i][j] == 0 and board[i][j+1] == 0: # 가로줄이 원래 없고, 다음 가로줄이 없을 때
                if board[i][j-1] == 1: # 이전 가로줄이 있으면 pass
                    continue
                board[i][j] = 1
                dfs(cnt + 1, i, j+2) # 연속된 가로선을 만들지 않기 위해 j + 2호출
                board[i][j] = 0 

        

min_val = 4
dfs(0,0,0)
print(min_val if min_val < 4 else -1)






