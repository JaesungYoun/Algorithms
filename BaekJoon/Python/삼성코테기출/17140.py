from collections import Counter
r,c,k = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(3)]


def rc():
    max_len = 0
    len_A = len(A)
    for j in range(len_A):
        a = [i for i in A[j] if i != 0]
        a = Counter(a).most_common()
        a.sort(key = lambda x:(x[1],x[0]))
        A[j] = []
        for num, cnt in a:
            A[j].append(num)
            A[j].append(cnt)
            if len(A[j]) >= 100:
                break
            
        
        max_len = max(max_len,len(A[j]))
    for j in range(len_A):
        for k in range(max_len-len(A[j])):
            A[j].append(0)
        

time = 0
result = -1
while time <= 100:
    
    try:
        if A[r-1][c-1] == k:
            result = time
            break
    except:
        pass
    if len(A) < len(A[0]):
        A = list(zip(*A))
        rc()
        A = list(zip(*A))
    else:
        rc()
    time += 1
print(result)