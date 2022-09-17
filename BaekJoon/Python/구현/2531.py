import sys
from collections import defaultdict
N,d,k,c = map(int,sys.stdin.readline().split())

chobob = []

for _ in range(N):
    chobob.append(int(sys.stdin.readline().rstrip()))


lp, rp = 0, 0
answer = 0

while lp != N:
    rp = lp + k
    case = set()
    addable = True
    for i in range(lp, rp):
        case.add(chobob[i%N])
        if chobob[i%N] == c: addable = False

    cnt = len(case)
    if addable: cnt += 1
    answer = max(answer, cnt)
    lp += 1

print(answer)

    