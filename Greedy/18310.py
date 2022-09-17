import sys

N = int(sys.stdin.readline())

pos = sorted(list(map(int,sys.stdin.readline().split())))

print(pos[(N-1)//2])

