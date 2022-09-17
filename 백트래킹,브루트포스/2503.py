from itertools import permutations
import sys

N = int(sys.stdin.readline())

all_case = list(permutations([i for i in range(1,10)],3))

for _ in range(N):
    q, s, b = map(int,sys.stdin.readline().split())
    q = list(str(q))
    count = 0 
    for i in range(len(all_case)):
        strike = 0 
        ball = 0
        i -= count
        for j in range(3):
            if all_case[i][j] == int(q[j]):
                strike += 1
            elif int(q[j]) in all_case[i]:
                ball += 1
        
        if strike != s or ball != b:
            all_case.remove(all_case[i])
            count += 1
            
print(len(all_case))