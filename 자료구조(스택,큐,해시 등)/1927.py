import sys
import heapq
N = int(sys.stdin.readline())

oper = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(oper) == 0:
            print(num)
        else:
            print(heapq.heappop(oper))
    else:
        heapq.heappush(oper,num)

    
    

    