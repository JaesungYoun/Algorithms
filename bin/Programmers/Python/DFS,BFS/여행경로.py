from collections import deque, defaultdict
def solution(tickets):
    answer = []
    
    
    tickets = sorted(tickets, key = lambda x : (x[1])) 
    dict = defaultdict(list)
    for k,v in tickets:
        dict[k].append(v)
    
    def dfs():
        stack = ["ICN"]
        while stack:
            airport = stack[-1]
            if airport not in dict or not dict[airport] :
                answer.append(stack.pop())
            else :
                stack.append(dict[airport].pop(0))
    dfs()
    return answer[::-1]