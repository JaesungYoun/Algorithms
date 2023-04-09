import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
bus_info = [[]for _ in range(N+1)]
for _ in range(M):
    a,b,w = map(int,sys.stdin.readline().split())
    bus_info[a].append([b,w])

start,end = map(int,sys.stdin.readline().split())

dist = [1e9]*(N+1) # 최소 비용 테이블


def dijkstra(start):
    queue = []
    
    heapq.heappush(queue,(0,start))
    dist[start] = 0
    
    
    while queue:
        d,now = heapq.heappop(queue) # 비용(우선순위), 현재 노드
        
        if dist[now] < d: # 이미 방문한 노드면 pass, 시간을 줄이기 위함 
            continue
        
        for i in bus_info[now]:
            if d + i[1] < dist[i[0]]:
                dist[i[0]] = d+i[1]   
                heapq.heappush(queue, (d + i[1], i[0]))

        
dijkstra(start)
print(dist[end])