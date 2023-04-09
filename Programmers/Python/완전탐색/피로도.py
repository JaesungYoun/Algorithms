
result = 0
def dfs(depth,k,dungeons,visited):
    global result
    
    if k <= 0:
        return
    
    result = max(result,depth)

    for i in range(len(dungeons)):
        if visited[i]:
            continue
        if k < dungeons[i][0]:
            continue
        visited[i] = True
        dfs(depth+1,k-dungeons[i][1],dungeons,visited)
        visited[i] = False


def solution(k, dungeons):
    answer = -1
    visited = [False] * (len(dungeons) + 1)
    dfs(0,k,dungeons,visited)

    
    return result


            
            
            
    
    
    
    