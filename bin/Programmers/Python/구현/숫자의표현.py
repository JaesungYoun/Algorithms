def solution(num):
    answer = 0
    for i in range(1, num+1):
        summ = 0
        while (summ < num):
            summ += i
            i += 1
        if summ == num:
            answer += 1
    return answer