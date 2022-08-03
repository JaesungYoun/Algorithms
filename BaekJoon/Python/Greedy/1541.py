import sys

oper = sys.stdin.readline().rstrip().split("-")

for i in range(len(oper)):
    sum = 0
    for j in oper[i].split("+"):
        sum += int(j)
    oper[i] = sum
result = oper[0]
for i in oper[1:]:
    result -= int(i)
    
print(result)