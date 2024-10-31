
def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    answer = 0
    end = 0  # 마지막으로 요격한 미사일의 x좌표

    for s, e in targets:
        if s >= end:  
            answer += 1
            end = e  
    return answer