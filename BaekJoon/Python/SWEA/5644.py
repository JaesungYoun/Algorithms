from collections import defaultdict
T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    M,A = map(int,input().split())
    a_info = [0] + list(map(int,input().split()))
    b_info = [0] + list(map(int,input().split()))
    BC_info = []
    mat = [[0] * 11 for _ in range(11)]
    num_ch = defaultdict(list)
    dx = [0,0,1,0,-1]
    dy = [0,-1,0,1,0]
    for _ in range(A):
        BC_info.append(list(map(int,input().split())))

    # 충전 범위
    for i in range(1,11):
        for j in range(1,11):
            for k in range(len(BC_info)):
                if abs(i-BC_info[k][0]) + abs(j-BC_info[k][1]) <= BC_info[k][2]:
                    mat[i][j] = max(mat[i][j],BC_info[k][3])
                    num_ch[(i,j)].append([k+1,BC_info[k][3]])
    
    for v in num_ch.values():
        v.sort(key = lambda x:(x[1]),reverse=True)
    
    power_a = 0
    power_b = 0
    # 사용자 좌표
    a_x,a_y = 1,1
    b_x,b_y = 10,10
    
    for i,j in zip(a_info,b_info):
        
        
        if 1<=a_x+dx[i]<=10 and 1<=a_y+dy[i]<=10:
            a_x += dx[i]
            a_y += dy[i]
            
        if 1<=b_x+dx[j]<=10 and 1<=b_y+dy[j]<=10:
            b_x += dx[j]
            b_y += dy[j]
         
        if mat[a_x][a_y] != 0 and mat[b_x][b_y] == 0:
            power_a += mat[a_x][a_y]
        elif mat[a_x][a_y] == 0 and mat[b_x][b_y] != 0:
            power_b += mat[b_x][b_y]
        elif mat[a_x][a_y] != 0 and mat[b_x][b_y] != 0:
            if len(num_ch[(a_x,a_y)]) > 1 and len(num_ch[(b_x,b_y)]) == 1: # A가 속한 구역이 1개이상, B가 속한 구역이 1개
                if num_ch[(a_x,a_y)][0][0] != num_ch[(b_x,b_y)][0][0]:
                    power_b += mat[b_x][b_y]
                    power_a += num_ch[(a_x,a_y)][0][1]
                else:
                    power_a += num_ch[(a_x,a_y)][1][1] 
                    power_b += mat[b_x][b_y]
            elif len(num_ch[(b_x,b_y)]) > 1 and len(num_ch[(a_x,a_y)]) == 1:       
                if num_ch[(a_x,a_y)][0][0] != num_ch[(b_x,b_y)][0][0]:
                    power_b += num_ch[(b_x,b_y)][0][1]
                    power_a += mat[a_x][a_y]
                else:
                    power_a += mat[a_x][a_y]
                    power_b += num_ch[(b_x,b_y)][1][1]
            elif len(num_ch[(a_x,a_y)]) > 1 and len(num_ch[(b_x,b_y)]) > 1:
                if num_ch[(a_x,a_y)][0][0] != num_ch[(b_x,b_y)][0][0]:
                    power_b += num_ch[(b_x,b_y)][0][1]
                    power_a += num_ch[(a_x,a_y)][0][1]
                else:
                    if num_ch[(a_x,a_y)][0][1] + num_ch[(b_x,b_y)][1][1] > num_ch[(b_x,b_y)][0][1] + num_ch[(a_x,a_y)][1][1]:
                        power_a += num_ch[(a_x,a_y)][0][1]
                        power_b += num_ch[(b_x,b_y)][1][1]
                    else:
                        power_a += num_ch[(a_x,a_y)][1][1]
                        power_b += num_ch[(b_x,b_y)][0][1]        
            elif len(num_ch[(a_x,a_y)]) == 1 and len(num_ch[(b_x,b_y)]) == 1:
                if num_ch[(a_x,a_y)][0][0] != num_ch[(b_x,b_y)][0][0]:
                    power_b += mat[b_x][b_y]
                    power_a += mat[a_x][a_y]
                else:
                    power_b += (mat[b_x][b_y] // 2)
                    power_a += (mat[a_x][a_y] // 2)         
                    
    print(power_a + power_b)
