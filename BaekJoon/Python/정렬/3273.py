import sys

n = int(sys.stdin.readline())
num = sorted(list(map(int,sys.stdin.readline().split())))
x = int(sys.stdin.readline())

answer = 0

def binary():
    global answer
    start, end = 0, n-1
    while start < end:
        _sum = num[start] + num[end]
        if _sum == x:
            answer += 1
            end -= 1
        elif _sum < x:
            start += 1
        else:
            end -= 1
    
    return answer

print(binary())


    