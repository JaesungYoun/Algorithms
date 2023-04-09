def dfs(start,mat,visited):
    visited[start] = True
    
    for i in mat[start]:
        if not visited[i]:
            dfs(i,mat,visited)
            
    

def solution(n, computers):
    answer = 0
    
    mat = [[] * (n) for _ in range(n)]
    
    for i in range(len(computers)):
        for idx,j in enumerate(computers[i]):
            if i == idx:
                continue
            if j == 1 and i not in mat[idx] and idx not in mat[i]:
                mat[i].append(idx)
                mat[idx].append(i)
    visited = [False] * n
    
    cnt = 0
    for start in range(n):
        if not visited[start]:
            dfs(start,mat,visited)
            cnt += 1
    
            
    answer = cnt
    return answer
