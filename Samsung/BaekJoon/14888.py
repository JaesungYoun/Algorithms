N = int(input())

a = list(map(int,input().split()))

oper = list(map(int,input().split()))

def backtracking(idx,total,add,sub,mul,div):
    global min_answer, max_answer
    if idx == N:
        min_answer = min(total,min_answer)
        max_answer = max(total,max_answer)
        return
    if add > 0:
        backtracking(idx + 1,total + a[idx], add - 1, sub, mul, div)
    if sub > 0:
        backtracking(idx + 1,total - a[idx], add, sub - 1, mul, div)
    if mul > 0:
        backtracking(idx + 1,total * a[idx], add, sub, mul - 1, div)
    if div > 0:
        if total < 0:
            backtracking(idx + 1, -(abs(total) // a[idx]),add,sub,mul,div-1)
        else:
            backtracking(idx + 1, total // a[idx], add, sub, mul, div - 1)

min_answer = 1e9
max_answer = -1e9

backtracking(1,a[0],oper[0],oper[1],oper[2],oper[3])
print(max_answer)
print(min_answer)
