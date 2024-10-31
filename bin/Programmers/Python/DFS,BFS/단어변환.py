from collections import deque



    


def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return answer
    
    words.append(begin)
    begin_idx = words.index(begin)
    target_idx = words.index(target)
    mat = [[] * len(words) for _ in range(len(words))]
    
    for idx1,i in enumerate(range(len(words))):
        for idx2,j in enumerate(range(len(words))):
            cnt = 0 
            for k in range(len(words[i])):
                if words[i][k] != words[j][k]: 
                    cnt += 1
            if cnt == 1:
                
                mat[idx1].append(idx2)
                mat[idx2].append(idx1)

    visited = [0] * len(words)
    def bfs(start,target_idx):
        queue = deque([start])
        visited[start] = 1
        
        while queue:
            v = queue.popleft()
            
            for i in mat[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = visited[v] + 1
                    
        return visited[target_idx] - 1
    
    answer = bfs(begin_idx,target_idx)
    
    
    return answer