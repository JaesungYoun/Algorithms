def solution(s):
    
    if len(s) <= 1:
        return 0
    
    stk = []
    idx = 0
    while idx < len(s):
        if stk:
            if stk[-1] == s[idx]:
                stk.pop()
            else:
                stk.append(s[idx])
            
        else:
            stk.append(s[idx])
        idx += 1
        
    if not stk:
        return 1
    else:
        return 0
    