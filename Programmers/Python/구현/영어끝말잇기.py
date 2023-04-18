def solution(n, words):
    answer = [0,0]

    cnt = 0
    check = []
    check.append(words[0])
    for i in range(1,len(words)):
        cnt += 1
        
        if words[i] not in check and check[-1][-1] == words[i][0]:
            check.append(words[i])
        else:  # (fail)
            answer[0] = cnt % n + 1  # 탈락번호
            answer[1] = cnt // n + 1  # 탈락차례
            break
        
    return answer