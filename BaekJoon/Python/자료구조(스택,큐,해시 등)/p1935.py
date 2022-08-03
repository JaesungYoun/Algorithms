import sys

N = int(input())

word = input()
nums = []

for i in range(N):
    nums.append(int(input()))

stk = []

for i in word:
    if 'A' <= i <= 'Z':
        stk.append(nums[ord(i)-ord('A')])
        
    
    else:
        y = stk.pop()
        x = stk.pop()
        
        if i == '+':
            stk.append(x+y)
        elif i == '-':
            stk.append(x-y)
        elif i == '*':
            stk.append(x*y)
        elif i == '/':
            stk.append(x/y)
        
print(f'{stk[0]:.2f}')