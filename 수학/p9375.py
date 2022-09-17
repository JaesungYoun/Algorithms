import sys
from collections import defaultdict


t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    fasion_list = defaultdict(list)
    day = 0
    for j in range(n):
        fasion = sys.stdin.readline().strip().split()
        fasion_list[fasion[1]].append(fasion[0])
    
    temp = 1
    for i in fasion_list.values():
        temp *= (len(i) + 1)
    day = temp - 1
    print(day)