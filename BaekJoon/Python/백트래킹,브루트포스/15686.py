import sys
from itertools import combinations
N,M= map(int,sys.stdin.readline().split())

mat = []
for _ in range(N):
    mat.append(list(map(int,sys.stdin.readline().split())))

    
    
home = []
chicken = []
for i in range(N):
    for j in range(N):
        if mat[i][j] == 1:
           home.append((i,j))
        elif mat[i][j] == 2:
            chicken.append((i,j))
                        

res = 1e9

cc = list(combinations(chicken,M))
city_dist = 1e9
for i in cc:
    temp = 0
    for h in home: 
       dist = 1e9
       for c in i:
           dist = min(dist,abs(c[0]-h[0])+abs(c[1]-h[1])) 
       temp += dist
    city_dist = min(city_dist,temp)
print(city_dist)

                
                
                
                