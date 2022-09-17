import sys

N = int(sys.stdin.readline())

arr = []
maxL = 0
maxH = 1

for _ in range(N):
    L,H = list(map(int,sys.stdin.readline().split()))
    arr.append([L,H])
    if maxL < L:
        maxL = L
    if maxH < H:
        maxH = H
        maxIndex = L

pillar = [0] * (maxL + 1)
for l,h in arr:
    pillar[l] = h

res = 0
temp = 0
for i in range(maxIndex + 1):
    if pillar[i] > temp:
        temp = pillar[i]
    res += temp
temp = 0
for i in range(maxL,maxIndex,-1):
    if pillar[i] > temp:
        temp = pillar[i]
    res += temp
print(res)