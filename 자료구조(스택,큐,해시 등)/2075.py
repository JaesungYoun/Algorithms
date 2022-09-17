import sys
import heapq

N = int(sys.stdin.readline())

heap = []
for _ in range(N):
    graph=list(map(int,sys.stdin.readline().split()))
    
    if not heap:
        for g in graph:
            heapq.heappush(heap,g)
    else:
        for g in graph:
            if heap[0] < g:
                heapq.heappush(heap,g)
                heapq.heappop(heap)
    print(heap)
                
print(heap)
print(heap[0])
  
  