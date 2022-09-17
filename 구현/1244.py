import sys

n = int(input())

sw = [-1 for _ in range(n+1)]
sw[1:] = list(map(int,sys.stdin.readline().strip().split()))

student_num = int(sys.stdin.readline())

def change_switch(i):
    if sw[i] == 0:
        sw[i] = 1
    else:
        sw[i] = 0
    return


for i in range(student_num):
    sex,num = map(int,sys.stdin.readline().split())
    if sex == 1:
        for i in range(num,n+1,num):
            change_switch(i)
    
    else:        
        change_switch(num)
        for j in range(n//2):
            if num + j > n or num - j < 1:
                break
            if sw[num+j] == sw[num-j]:
                change_switch(num+j)
                change_switch(num-j)
            else:
                break

cnt = 0
for i in range(1,n+1):
    print(sw[i], end = " ")
    if i % 20 == 0:
        print()