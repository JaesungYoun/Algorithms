import sys

n = int(sys.stdin.readline())

for _ in range(n):
    key = sys.stdin.readline().strip()
    stk = []
    temp = []
    for i in range(len(key)):
        if key[i] == '<' and stk:
            temp.append(stk.pop())
        elif key[i] == '>' and temp:
            stk.append(temp.pop())
        elif key[i] == '-' and stk:
            stk.pop()
        elif not (key[i] == '<' or key[i] == '>' or key[i] =='-'): 
            stk.append(key[i])
    
    print(''.join(stk + list(reversed(temp))))