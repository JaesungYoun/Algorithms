import sys
from collections import deque

t = int(sys.stdin.readline())


for i in range(t):
    n,m = map(int,sys.stdin.readline().split())
    importance = list(map(int,sys.stdin.readline().split()))
    queue = deque([])
    for i in range(n):
        queue.append(0)
    
    count = 0
    while queue:
        
        if importance[0] != max(importance):
            
            if m > 0:
                m -= 1
            elif m == 0:
                m = len(queue) - 1
            queue.append(queue.popleft())
            importance.append(importance.pop(0))
        else:
            count += 1
            if m == 0:
                print(count)
                break
            elif m > 0:
                m -= 1
                queue.popleft()
                importance.pop(0)
    
    