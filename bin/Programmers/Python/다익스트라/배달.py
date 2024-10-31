import heapq

def solution(N, road, K):
    answer = 0
    
    if N == 1:
        return 1
    
    n = N
    visited = [False] * (n+1)
    distance = [1e9] * (n+1)
    graph = [[] for _ in range(n+1)]
    for r1,r2,dist in road:
        graph[r1].append((r2,dist))
        graph[r2].append((r1,dist))
    
    def get_smallest_node():
        min_val = 1e9
        index = 1
        for i in range(1,n+1):
            if distance[i] < min_val and not visited[i]:
                min_val = distance[i]
                index = i
        return index
    
    
    def dikjstra(start):
        q = []
        heapq.heappush(q, (0,start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now]<dist:
                continue
            for i in graph[now]:
                cost = dist+i[1]
                if cost<distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost,i[0]))
    
    dikjstra(1)
    for i in range(1,len(distance)):
        if distance[i] <= K:
            answer += 1
    return answer