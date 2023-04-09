from collections import deque
N,K = map(int,input().split())

a = deque(list(map(int,input().split())))
robot = deque([0] * N)
t = 0

while 1:

    # 1. 회전
    a.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    # 2. 로봇, 벨트 회전
    for i in range(N-2,-1,-1):
        if robot[i] == 1 and robot[i+1] == 0 and a[i+1] >= 1:
            robot[i+1] = 1
            robot[i] = 0
            a[i+1] -= 1
        
        robot[-1] = 0

    # 3. 로봇 올리기
    if robot[0] == 0 and a[0] >= 1:
        robot[0] = 1
        a[0] -= 1
    t += 1
    # 4. 체크
    if a.count(0) >= K:
        break
print(t)