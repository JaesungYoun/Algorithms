import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    grades = []
    for _ in range(N):
        gd1,gd2 = map(int,sys.stdin.readline().split())
        grades.append([gd1,gd2])
    grades = sorted(grades,key = lambda x : x[0])
    
    temp = grades[0][1]
    cnt = 1
    for i in range(len(grades)):
        if temp > grades[i][1]:
            cnt += 1
            temp = grades[i][1]
            
            
    print(cnt)