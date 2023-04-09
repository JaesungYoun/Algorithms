import sys

L,C = map(int,sys.stdin.readline().split())

alphabets = list(map(str,sys.stdin.readline().split()))

alphabets.sort()
vowel = ['a','e','i','o','u']
output = []
visited = [False] * (C+1)
def backtracking(depth,idx):
    if depth == L:
        co,vo = 0,0
        for i in range(L):
            if output[i] in vowel:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print("".join(output))
        return
    
    for i in range(idx,C):
    
        
        output.append(alphabets[i])
        backtracking(depth + 1, i + 1)
        output.pop()
        
backtracking(0,0)