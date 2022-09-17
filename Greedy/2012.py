import sys

N = int(sys.stdin.readline())

rank = []

for i in range(N):
    rank.append(int(sys.stdin.readline()))

rank.sort()
real_rank = [i for i in range(1,N+1)]
diff = 0

for i,j in zip(rank,real_rank):
    diff += abs(i - j)

print(diff)

