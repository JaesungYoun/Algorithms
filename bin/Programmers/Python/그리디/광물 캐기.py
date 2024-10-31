def solution(picks, minerals):
    answer = 0
    sum = 0
    for x in picks:
        sum += x
    
    # 캘 수 있는 광물의 개수
    num_min = sum * 5
    if len(minerals) > num_min: # 주어진 광물이 캘 수 있는 광물 수보다 크면
        minerals = minerals[:num_min]
        
    # 광물 조사
    arr = [[0,0,0] for _ in range(10)]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            arr[i//5][0] += 1
        if minerals[i] == 'iron':
            arr[i//5][1] += 1
        if minerals[i] == 'stone':
            arr[i//5][2] += 1
    
    arr = sorted(arr,key = lambda x: (-x[0],-x[1],-x[2]))
    
    
    
    for minerals in arr:
        d,i,s = minerals
        idx = 0    
        while 1:
            if not picks[idx] and idx == 2:
                break
            if picks[idx] == 0:
                idx += 1
                continue
                
            
            
            if idx == 0:
                answer += d + i + s
            elif idx == 1:
                answer += 5 * d + i + s
            elif idx == 2:
                answer += 25 * d + 5 *i + s
                
            picks[idx] -= 1
            break
    
    
    
            
    return answer