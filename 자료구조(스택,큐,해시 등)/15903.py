import sys
import heapq

n,m = map(int,sys.stdin.readline().split())

nums = list(map(int,sys.stdin.readline().split()))

heap = []

for i in nums:
    heapq.heappush(heap,i)

for _ in range(m):
    n1 = heapq.heappop(heap)
    n2 = heapq.heappop(heap)
    
    heapq.heappush(heap,n1+n2)
    heapq.heappush(heap,n1+n2)

print(sum(heap))    