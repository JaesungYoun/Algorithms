import sys

s = sys.stdin.readline().strip()

stk = []
all = []
temp = []
for i in s:
    
    if i == '<':
        stk.append(i)
        if len(temp) > 0:
            all.append(''.join(temp)[::-1])
            temp = []
            
        
        all.append(i)
    elif i == '>':
        stk.pop()
        all.append(i)
    else:
        if len(stk) == 0:
            if i == ' ':
                all.append(''.join(temp)[::-1])
                temp = []
                all.append(' ')
            else:
                temp.append(i)
        else:
            all.append(i)
all.append(''.join(temp)[::-1])
print(''.join(all))
