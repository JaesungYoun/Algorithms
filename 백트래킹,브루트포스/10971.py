import sys

N = int(sys.stdin.readline())

city = []
for _ in range(N):
    city.append(list(map(int,sys.stdin.readline().split())))

ans = sys.maxsize
visited = [0] * N
def dfs(start,now,cost,cnt):
    global ans
    if cnt == N:
        if city[now][start]:
            cost += city[now][start]
            if ans > cost:
                ans = cost
        return
    if cost > ans:
        return
    
    
    for i in range(N): 
        if visited[i] == 0 and city[now][i]:
            visited[i] = 1   
            # cost += city[now] 
            # cost += city[now]  이것만은 안된다, 반복문을 한 함수에서 여러번 돌기 떄문
            dfs(start,i,cost+city[now][i],cnt+1) 
            # cost -= city[now]  마이너스도 같이 해줘야함
            visited[i] = 0

for i in range(N):
    visited[i] = 1
    dfs(i,i,0,1)
    visited[i] = 0

print(ans)