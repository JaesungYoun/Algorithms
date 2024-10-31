def solution(elements):
    answer = 0
    
    visited = set()
    n = len(elements)
    length = 1
    for _ in range(n):
        for i in range(n):
            if i + length <= n:
                visited.add(sum(elements[i:i+length]))
            else:
                visited.add(sum(elements[i:]) + sum(elements[:(i + length) % n]))
        length += 1
    answer = len(visited)
    
    
    return answer