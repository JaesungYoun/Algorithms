# 23290 마법사 상어와 복제

import copy

def turn(d):
    return (d + 1) % 8

def move_fish(arr,shark_r, shark_c):
    
    
    for r in range(1,5):
        for c in range(1,5):
            for idx in range(1,9):
                if arr[r][c][0] != 0:
                    d = arr[r][c][1]
                    for _ in range(8):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if 1<=nr<=4 and 1<=nc<=4 and (nr != shark_r and nc!= shark_c) and smell[nr][nc] == 0:
                            arr[nr][nc] = [1,d]
                            arr[r][c] = [0,0]
                            break
                        d = turn(d)
                            
    
    
#     0 좌 좌상 상 우상 우 우하 하 좌하
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 0, 상 좌 하 우
shark_dr = [0, -1, 0, 1, 0]
shark_dc = [0, 0, -1, 0, 1]

M, S = map(int, input().split())
grounds = [[0,0] * 5 for _ in range(5)]
smell = [[0] * 5 for _ in range(5)]
for _ in range(M):
    r, c, d = map(int, input().split())
    grounds[r][c] = [1,d]

shark_r, shark_c = map(int, input().split())

for idx in range(1,S+1):
    
    # 1. 복제 마법 
    copy_list = [[0,0] * 5 for _ in range(5)]
    for r in range(1,5):
        for c in range(1,5):
            copy_list[r][c] = grounds[r][c]
    
    # 2. 모든 물고기 한 칸 이동
    move_fish(grounds,shark_r,shark_c)
    
    # 3. 상어가 연속해서 3칸 이동
    choice = []
    max_val = 0
    temp_shark_r = 0
    temp_shark_c = 0
    
    temp_grounds_list = [[0,0] * 5 for _ in range(5)]
    for r in range(1,5):
        for c in range(1,5):
            temp_grounds_list[r][c] = grounds[r][c]
    
    for i in range(1,5):
        nr1 = shark_r + shark_dr[i]
        nc1 = shark_c + shark_dc[i]
        if not (1<=nr1<=4 and 1<=nc1<=4):
            continue
        sum1 = sum(temp_grounds_list[nr1][nc1][0])
        for j in range(1,5):
            
    
    # 4. 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라짐
    for r in range(1, 5):
        for c in range(1, 5):
            if smell[r][c] + 2 <= idx: # 두 번 전
                smell[r][c] = 0
    
    # 5. 복제 마법 완료
    for r in range(1,5):
        for c in range(1,5):
            grounds[r][c][0] += copy_list[r][c][0]
            
            
result = 0
for r in range(1,5):
    for c in range(1,5):
        result += grounds[r][c][0]
        
print(result)
 