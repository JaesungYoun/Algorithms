

result = []
def dfs(depth,alpha,w,visited):
    global result

    result.append(w)
    
    if result == w:
        return
    
    if depth == 5:
        return
    
    for i in range(len(alpha)):
        dfs(depth + 1, alpha,w + alpha[i],visited)
        


def solution(word):
    global result
    answer = 0    
    alpha = ['A', 'E', 'I', 'O', 'U']
    visited = [False] * (len(alpha) )
    dfs(0,alpha,'',visited)
    
    answer = result.index(word)
    
    return answer



        
        
    
    
    
    