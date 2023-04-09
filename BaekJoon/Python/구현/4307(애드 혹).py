import sys

t = int(sys.stdin.readline())

for _ in range(t):
    stick, n = map(int,sys.stdin.readline().split())
    pos = []
    for i in range(n):
        pos.append(int(sys.stdin.readline()))
    pos.sort()
    
    dist_from_mid = stick
    temp = 0 
    max_time = 0
    for i in range(len(pos)):
        if abs((stick // 2) - pos[i]) < dist_from_mid: 
            dist_from_mid = (stick // 2) - pos[i]
            temp = pos[i]
        max_time = max(max_time,pos[i],stick-pos[i])
    print(min(abs(stick - temp),temp),max_time)
    
    
    
    
    