import sys

w,h = map(int,sys.stdin.readline().split())

n = int(sys.stdin.readline())

pos = []

for _ in range(n+1):
    pos.append(list(map(int,sys.stdin.readline().split())))



res = 0
for i in range(n):
    dist = 0
    if pos[-1][0] == 1:
        if pos[i][0] == 1:
            dist = abs(pos[-1][1] - pos[i][1])
        elif pos[i][0] == 2:
            left = pos[-1][1] + h + pos[i][1]
            right = (w - pos[-1][1]) + h + (w-pos[i][1])
            dist = min(left,right)
        elif pos[i][0] == 3:
            dist = pos[-1][1] + pos[i][1]
        elif pos[i][0] == 4:
            dist = (w-pos[-1][1] + pos[i][1])        
    elif pos[-1][0] == 2:
        if pos[i][0] == 1:
            left = pos[-1][1] + h + pos[i][1]
            right = (w - pos[-1][1]) + h + (w - pos[i][1])
            dist = min(left, right)
        elif pos[i][0] == 2:
            dist = abs(pos[-1][1] - pos[i][1])
        elif pos[i][0] == 3:
            dist = abs(pos[-1][1] + (h - pos[i][1]))
        elif pos[i][0] == 4:
            dist = (w - pos[-1][1]) + (h - pos[i][1])
    elif pos[-1][0] == 3:
        if pos[i][0] == 1:
            dist = (pos[-1][1] + pos[i][1])
        elif pos[i][0] == 2:
            dist = (h - pos[-1][1]) + pos[i][1]
        elif pos[i][0] == 3:
            dist = abs(pos[-1][1] - pos[i][1])
        elif pos[i][0] == 4:
            left = pos[-1][1] + w + pos[i][1]
            right = (h - pos[-1][1]) + w + (h - pos[i][1])
            dist = min(left, right)
    elif pos[-1][0] == 4:
        if pos[i][0] == 1:
            dist = pos[-1][1] + (w - pos[i][1])
        elif pos[i][0] == 2:
            dist = (h - pos[-1][1]) + (w - pos[i][1])
        elif pos[i][0] == 3:
            left = (h - pos[-1][1]) + w + (h - pos[i][1])
            right = pos[-1][1] + w + pos[i][1]
            dist = min(left, right)
        elif pos[i][0] == 4:
            dist = abs(pos[-1][1] - pos[i][1])
    res += dist
    
print(res)