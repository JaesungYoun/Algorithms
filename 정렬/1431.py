import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    s = sys.stdin.readline().strip()
    arr.append(s)


def sum_num(s):
    n = 0
    for i in s:
        if i.isdigit():
            n += int(i)
    return n

arr = sorted(arr, key = lambda x: (len(x),sum_num(x),x))

for i in arr:
    print(i)