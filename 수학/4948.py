import sys


def is_prime(num):
    
    if num == 1:
        return False
    
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    
    return True

all_num = list(range(2,246912))
result = []
for i in all_num:
    if is_prime(i):
        result.append(i)

while 1:
    num = int(sys.stdin.readline())
    if num == 0:
        break
    cnt = 0
    for i in result:
        if num < i <= 2*num:
            cnt += 1
    print(cnt)
    
    