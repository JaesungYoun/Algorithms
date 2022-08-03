import sys
sys.setrecursionlimit(10**7)
T = int(sys.stdin.readline())

def dfs(x,y):
    if not (0 <= x < M and 0 <= y < N):
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

graph = [[0] * (50) for _ in range(50)]

for _ in range(T):
    cnt = 0
    M,N,K = map(int,sys.stdin.readline().split())
    for i in range(K):
        x,y = map(int,sys.stdin.readline().split())
        graph[x][y] = 1
    for i in range(M):
        for j in range(N):
            if dfs(i,j) == True:
                cnt +=1 
            
    print(cnt)
    graph = [([0] * 51 )for _ in range(51)]


    


   
    
    