def solution(number, k):
    answer = []
    stk = []
    
    for i in range(len(number)):
        while stk and stk[-1] < number[i] and k > 0:
            k -= 1
            stk.pop()
            
        
        stk.append(number[i])
    
    answer = ''.join(stk[:len(number)-k])
    
    return answer