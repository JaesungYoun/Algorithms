from sys import stdin

n, p = map(int, stdin.readline().strip().split())
data = [[] for _ in range(7)]
result = 0

for _ in range(n):
    num, melody = map(int, stdin.readline().strip().split())
    if data[num] and data[num][-1] == melody:
        continue
    while data[num] and data[num][-1] > melody:
        data[num].pop()
        result += 1
    if data[num] and data[num][-1] == melody:
        continue
    data[num].append(melody)
    result += 1

print(result)
