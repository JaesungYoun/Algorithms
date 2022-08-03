import sys
from collections import defaultdict

K,L = map(int,sys.stdin.readline().split())
stu_num = defaultdict(int)

for i in range(L):
    stu_num[sys.stdin.readline().rstrip] = i

stu_num = sorted(stu_num.items(), key = lambda x:x[1])

cnt = 0
for i in stu_num:
    if cnt == K:
        break
    print(i[0])
    cnt += 1

        