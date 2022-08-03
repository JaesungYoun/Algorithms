import sys

N = int(sys.stdin.readline())

num_list = list(map(int,sys.stdin.readline().split()))
num_list.sort()
if N % 2 == 0:
    print(num_list[N//2 - 1])
else:
    print(num_list[N // 2])