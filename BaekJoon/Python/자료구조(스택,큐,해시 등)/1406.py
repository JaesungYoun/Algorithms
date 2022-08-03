import sys

s = list(sys.stdin.readline().strip())
M = int(sys.stdin.readline())
stk = []
for i in range(M):
    cmd = list(sys.stdin.readline().strip().split())
    if cmd[0] == 'L' and s:
       stk.append(s.pop())
    elif cmd[0] == 'D' and stk:
        s.append(stk.pop())
    elif cmd[0] == 'B' and s:
        s.pop()
    elif cmd[0] == 'P':
        s.append(cmd[1])
        
print(''.join(s + list(reversed(stk))))