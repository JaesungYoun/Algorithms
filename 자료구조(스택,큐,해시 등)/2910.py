import sys


N,C = map(int,sys.stdin.readline().split())

seq = list(map(int,sys.stdin.readline().split()))

seq = sorted(seq, key = lambda x: (-(seq.count(x)),seq.index(x)))

for i in seq:
    print(i, end = ' ')

