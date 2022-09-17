import sys
from collections import defaultdict

dic = defaultdict(int)
cnt = 0
while 1:
    
    s = sys.stdin.readline().rstrip()
    if not s:
        break

    dic[s] += 1
    cnt += 1
for i,j in sorted(dic.items()):
    percent = round((j/cnt)*100,4)
    print(i,'%.4f'%percent)
