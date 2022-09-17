import sys
from itertools import combinations
while 1:
    S = list(map(int,sys.stdin.readline().strip().split()))
    k = S[0]
    S = S[1:]
    if k == 0 :
        break
    c = list(combinations(S,6))
    for i in c:
        for j in i:
            print(j,end =' ')
        print()
    print()

        