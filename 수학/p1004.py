import sys
import math
T = int(sys.stdin.readline())

for i in range(T):
    count = 0 
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    for j in range(n):
        cx,cy,r = map(int,sys.stdin.readline().split())
        d1 = math.sqrt((x1-cx)**2 + (y1-cy)**2)
        d2 = math.sqrt((x2-cx)**2 + (y2-cy)**2)
        if (d1 < r and d2 > r) or (d1 > r and d2 < r): # 시작점과 출발점 중 하나는 원 밖, 하나는 원 안에 있어야 횟수가 증가
            count += 1
    print(count)
        
    