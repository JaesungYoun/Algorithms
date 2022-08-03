import sys

s = list(sys.stdin.readline().strip())
set_s = list(set(s))

temp = ''
result = ''
cnt = 0
for i in set_s:
    if s.count(i) % 2 == 1:
        cnt += 1

nc = [0 for _ in range(26)]

for i in s:
    nc[ord(i)-65] += 1

for i in range(26):
    if nc[i] % 2 == 1:
        temp = chr(i+65)
    result += chr(i+65) * (nc[i] // 2)

reverse_result = list(result)
reverse_result.reverse()


if cnt >= 2:
    print("I'm Sorry Hansoo")
else:
    print(result + temp + ''.join(reverse_result))
