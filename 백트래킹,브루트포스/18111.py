import sys
from collections import Counter,defaultdict
N,M,B = map(int,sys.stdin.readline().split())
h = []
for _ in range(N):
    h+= map(int,sys.stdin.readline().split())

h = dict(Counter(h))

def make_land(height):
    
    time = 0
    for i in h:
        if i < height:
            time += (height - i) * h[i]
        else:
            time += (i - height) * h[i] * 2
    
    return time

time = sys.maxsize
floor = 0
for i in range(257):
    max,min = 0,0
    
    for j in h.keys():
        if j < i:
            min += (i - j) * h[j]
        else:
            max += (j - i) * h[j]
    sec = make_land(i)
    
    inven = max + B
    if inven >= min:
        if sec <= time:
            time = sec
            floor = i

print(time,floor)