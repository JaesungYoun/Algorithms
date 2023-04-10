import math
def div(num):
    if num == 1:
        return 0
    
    
    temp = []
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            temp.append(i)
            if num // i < 10000001:
                return num // i
            
    if temp:
        return temp[len(temp)-1]
    return 1

def solution(begin, end):

    answer = []

    for i in range(begin, end + 1):
        answer.append(div(i))
                
        

    return answer