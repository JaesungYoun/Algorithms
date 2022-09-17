import sys
from itertools import permutations
k = int(sys.stdin.readline())

sign = list(sys.stdin.readline().strip().split())

num = [1,2,3,4,5,6,7,8,9,0]

per = list(permutations(num,k+1))

result = []
for p in per:
    flag = True
    for i in range(len(sign)):
        if sign[i] == '<':
            if p[i] < p[i+1]:
                continue
            else:
                flag = False
                break
        else:
            if p[i] > p[i+1]:
                continue
            else:
                flag = False
                break
    if flag:
        result.append(p)
    
print(''.join(map(str,list(max(result)))))
print(''.join(map(str,list(min(result)))))