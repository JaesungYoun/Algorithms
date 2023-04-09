from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    count = sorted(Counter(tangerine).items(), key = lambda x : x[1],reverse = True)
    
    for key, value in count:
        if k <= 0: # 이 조건이 중요! 
            break        
        k -= value # 계속 값을 빼준다
        answer += 1
    return answer