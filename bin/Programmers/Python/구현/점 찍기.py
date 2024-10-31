import math
def solution(k, d):
    answer = 0
    
    for x in range(0,d+1,k):
        res = math.floor(math.sqrt(d*d - x*x))
        answer += (res // k) + 1 
        

    return answer