import sys


input = sys.stdin.readline().strip()

stk = []
count = 0

for i in range(len(input)):
    if input[i] == '(':
        stk.append('(')
    else:
        if input[i-1] == '(':
            stk.pop()
            count += len(stk)
        else:
            stk.pop()
            count += 1
            
print(count)