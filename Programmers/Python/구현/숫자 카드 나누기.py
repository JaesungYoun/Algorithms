import math
def check(a,b):
    
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    
    temp = []
    if len(a) > 1:
        g = math.gcd(a[0],a[1])
        temp.append(g)
        if len(a) > 2:
            for i in range(2,len(a)):
                temp.append(math.gcd(g,a[i]))
    else:
        temp.append(a[0])
    answer = 0

    for k in temp:
        for i,j in zip(a,b):
            if i % k == 0 and j % k != 0:
                continue
            else:
                break
        else:
            answer = k
            return answer
                
    return 0

def solution(arrayA, arrayB):
    answer = 0
    answer = max(check(arrayA,arrayB), check(arrayB,arrayA))
    return answer