import sys
from itertools import combinations
import math
t = int(sys.stdin.readline())




for i in range(t):
    n = list(map(int,sys.stdin.readline().split()))[1:]
    c = list(combinations(n,2))
    temp = [] 
    for j in range(len(c)):
        temp.append(math.gcd(c[j][0],c[j][1]))
    
    
    print(sum(temp))
        
        