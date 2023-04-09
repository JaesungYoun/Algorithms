N = int(input())

arr = []
for _ in range(N):
    p,c = map(int,input().split())
    arr.append([c,p])

arr.sort()


now = arr[0][0]
index = 0
answer = 0
flag = False
while 1:
    if index == len(arr) - 1:
        answer += (arr[index][1] - arr[index-1][1]) 
        break
    
    if now == arr[index][0]:
        if not flag:
            index += 1
            answer += (arr[index][1] - arr[index-1][1])
            flag = True
        else:
            if now == arr[index+1][0]:
                answer += min(arr[index][1] - arr[index-1][1], arr[index+1][1] - arr[index][1])
            
            else:
                answer += arr[index][1] - arr[index-1][1]
                flag = False
            index += 1
            
    else:
        now = arr[index][0]
            
        flag = False
    
    
print(answer)