import sys
from collections import defaultdict

N = int(sys.stdin.readline())
dic = defaultdict(int)
point = list(map(int,sys.stdin.readline().strip().split()))
sort_point = sorted(list(set(point)))
for idx,i in enumerate(sort_point):
    dic[i] = idx
    
for i in point:
    print(dic[i], end = ' ')