import sys

N = int(sys.stdin.readline())

M = int(sys.stdin.readline())

S = sys.stdin.readline().rstrip()


ans = 0
cnt = 0
i = 1

while i < M - 1:
    if S[i-1] == "I" and S[i] == "O" and S[i+1] == "I":
        cnt += 1
        if cnt == N:
            cnt -= 1
            ans += 1
        i += 1
    else:
        cnt = 0
    i += 1

print(ans)
