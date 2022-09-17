import sys
from collections import defaultdict
N = int(sys.stdin.readline())

vote_num = int(sys.stdin.readline())

stu_num = list(map(int,sys.stdin.readline().split()))

dic = defaultdict(int)

for i in range(len(stu_num)):
    if len(dic) < N:
        dic[stu_num[i]] += 1
    else:
        if stu_num[i] not in dic.keys():
            s = sorted(dic.items(),key =lambda x:x[1])
            del[dic[s[0][0]]]
            dic[stu_num[i]] += 1
        else:
            dic[stu_num[i]] += 1
        

for i in sorted(dic.keys()):
    print(i, end = ' ')
        
