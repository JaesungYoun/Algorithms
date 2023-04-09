from collections import deque
def solution(queue1, queue2):
    
    if (sum(queue1) + sum(queue2)) % 2 == 1:
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    cnt = 0
    while 1:
        if cnt > 2 * (len(queue1) + len(queue2)):
            return -1
        
        if sum1 > sum2:
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num
            sum2 += num
            
        elif sum2 > sum1:
            num = queue2.popleft()
            queue1.append(num)
            sum1 += num
            sum2 -= num
        else:
            return cnt
        cnt += 1
                          