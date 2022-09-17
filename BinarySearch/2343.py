import sys

N,M = map(int,sys.stdin.readline().split())

lec = list(map(int,sys.stdin.readline().split()))

result = sum(lec)

def binary():
    global result
    start = max(lec)
    end = sum(lec)
    
    while start<=end:
        
        mid = (start + end) // 2
        temp = 0
        cnt = 1
        for i in range(len(lec)):
            if temp + lec[i] > mid:
                cnt += 1
                temp = 0
            temp += lec[i]
            
        if cnt <= M:
            end = mid - 1
            result = min(result,mid)
        else:
            start = mid + 1
    
    return result
print(binary())