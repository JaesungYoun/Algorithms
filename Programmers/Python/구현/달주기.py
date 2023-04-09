
t = int(input())
for _ in range(t):
    arr = list(map(int,input().split()))
    if len(arr) == 1:
        if arr[0] == 0:
            answer = 1
        elif arr[0] == 15:
            answer = 0
        else:
            answer = -1
    else:
        if arr[-2] > arr[-1]:
            if arr[-1] == 0:
                answer = 1
            else:
                answer = 0
        elif arr[-2] < arr[-1]:
            if arr[-1] == 15:
                answer = 0
            else:
                answer = 1

    print(answer)