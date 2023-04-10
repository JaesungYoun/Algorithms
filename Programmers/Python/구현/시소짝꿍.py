from collections import Counter
def solution(weights):
    answer = 0
    
    
    d = Counter(weights)
    for k,v in d.items():
        answer += v * (v-1) // 2
        for d1,d2 in [(2,3),(2,4),(3,4)]:
            answer += d[k*d1//d2] * v
    
    return answer