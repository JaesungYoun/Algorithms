def solution(plans):
    answer = []
    arr = []
    for plan in plans:
        name = plan[0]
        h, m = map(int, plan[1].split(':'))
        t = int(plan[2])
        arr.append((name, h*60 + m, t))

    arr.sort(key= lambda x : x[1])
    st = []
    for i in range(len(arr)-1):
        n, s, t = arr[i]
        if s + t <= arr[i+1][1]:
            answer.append(n)
            time_left = arr[i+1][1] - s - t # 새로운 과제 끝내고 남은 시간
            while st:
                name, time = st.pop()
                if time_left >= time:
                    time_left -= time
                    answer.append(name)
                else:
                    st.append((name, time - time_left))
                    break

        else:
            st.append((n, t - (arr[i+1][1] - s)))
    answer.append(arr[-1][0])

    while st:
        answer.append(st.pop()[0])
    return answer