import sys

k, d, N = map(str,sys.stdin.readline().split())
N = int(N)
row = [1,2,3,4,5,6,7,8]
col = ['A','B','C','D','E','F','G','H']
move = ['T','R','B','L','RT','LT','RB','LB']
# T, R, B, L, RT, LT, RB, LB
dx = [1,0,-1,0,1,1,-1,-1] 
dy = [0,1,0,-1,1,-1,1,-1]


king_x = row.index(int(k[1]))
king_y = col.index(k[0])
stone_x = row.index(int(d[1]))
stone_y = col.index(d[0])

for i in range(N):
    move_index = move.index(sys.stdin.readline().strip())
    
    nx = king_x + dx[move_index]
    ny = king_y + dy[move_index]
    
    if not (0<=nx<=7 and 0<=ny<=7):
        continue
    
    if nx == stone_x and ny == stone_y:
        stone_x = stone_x + dx[move_index]
        stone_y = stone_y + dy[move_index]
        
        if not (0<=stone_x<=7 and 0<=stone_y<=7): 
            stone_x -= dx[move_index]
            stone_y -= dy[move_index]
            continue
        
    king_x = nx
    king_y = ny
    
king_result = col[king_y] + str(row[king_x])
stone_result = col[stone_y] + str(row[stone_x])
print(king_result)
print(stone_result)