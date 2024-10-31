from collections import defaultdict
def solution(cards):
    answer = -1e9
    
    boxes = defaultdict(int)
    
    group = []
    
    for i,c in enumerate(cards):
        boxes[i+1] = c
        
    while boxes:
        opened = set() # 열린 상자 번호들의 집합
        cur = list(boxes.keys())[0]
        while cur not in opened:
            opened.add(cur)
            temp = boxes[cur] # 다음 번호 값을 저장
            del boxes[cur]
            cur = temp
        group.append(len(opened))
    group.sort(reverse = True)
    
    if len(group) > 1:
        return group[0] * group[1]
    else:
        return 0
    
    