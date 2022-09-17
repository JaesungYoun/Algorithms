import sys

n = int(sys.stdin.readline())

input = 1

stk = []
pm = []

for i in range(n):
    num = int(sys.stdin.readline())
    while input <= num:
        stk.append(input)
        input += 1
        pm.append("+")
    
    if stk[-1] == num:
        stk.pop()
        pm.append("-")
    else:
        print("NO")
        exit()
    

for i in pm:
    print(i)