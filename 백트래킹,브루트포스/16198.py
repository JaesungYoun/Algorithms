import sys

N = int(sys.stdin.readline())

w = list(map(int,sys.stdin.readline().split()))

def backtracking(energy):
    global res
    
    if len(w) == 2:
       res = max(res,energy)
       return

    for i in range(1,len(w)-1):
        temp = w[i-1] * w[i+1]
        
        removed = w.pop(i)
        backtracking(energy+temp)
        w.insert(i,removed)
res = 0
backtracking(0)
print(res)
        
