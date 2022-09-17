import sys
from collections import defaultdict
s = sys.stdin.readline().rstrip()

result = []
for i in range(1,len(s) + 1):
    for j in range(len(s) + 1 - i):
        result.append(s[j:j+i])
print(len(list(set(result))))

        