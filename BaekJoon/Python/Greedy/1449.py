import sys

N,L = map(int,sys.stdin.readline().split())

leak = list(map(int,sys.stdin.readline().strip().split()))
leak.sort()


start = leak[0]
end = start + L - 0.5 

cnt = 1

for i in range(len(leak)):
    if end >= leak[i]:
        continue
    else:
        cnt += 1
        end = leak[i] + L - 0.5
print(cnt)