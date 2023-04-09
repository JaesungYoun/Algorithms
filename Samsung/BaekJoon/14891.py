from collections import deque
import math
wheel_status = deque([-1])
for _ in range(4):
    wheel_status.append(deque(map(int,input())))

K = int(input())
rotate_info = []
for _ in range(K):
    rotate_info.append(list(map(int,input().split())))

for i in rotate_info: # 회전 횟수만큼
    num, dir = i[0],i[1]
    cnt_left = 0
    cnt_right = 0 
    temp = num
    for j in range(temp,1,-1):
        if wheel_status[j - 1][2] != wheel_status[j][6]: # 초기 상태를 저장하기 위해
            cnt_left += 1               # 먼저 회전을 해야하는 횟수를 세어줌
        else:
            break
    temp = num
    for j in range(temp,4,1):
        if wheel_status[j + 1][6] != wheel_status[j][2]:
            cnt_right += 1
        else:
            break


    wheel_status[num].rotate(dir)
    
    left_dir = dir * (-1)
    right_dir = dir * (-1)
    for j in range(num-1,num-cnt_left-1,-1):
        wheel_status[j].rotate(left_dir)
        left_dir *= -1

    for j in range(num+1,num+cnt_right+1):
        wheel_status[j].rotate(right_dir)
        right_dir *= -1 


point = 0
for i in range(1,len(wheel_status)):
    if wheel_status[i][0] == 1:
        point += int(math.pow(2,i-1))

print(point)
    


