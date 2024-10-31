N = int(input())

mat = []

for _ in range(N):
    mat.append(list(map(int,input().split())))

visited = [False] * N

def backtracking(depth,idx):
    global answer
    
    if depth == N // 2:
        start = 0
        link = 0

        for i in range(N):
            if visited[i]:
                for j in range(i+1,N):
                    if visited[j]:
                        start += mat[i][j]
                        start += mat[j][i]
            else:
                for j in range(i+1,N):
                    if not visited[j]:
                        link += mat[i][j]
                        link += mat[j][i]



        answer = min(answer, abs(start - link))
        
        if answer == 0:
            return
        return


    
    # 팀 나누기
    for i in range(idx,N):
        if visited[i]:
            continue
        visited[i] = True
        backtracking(depth + 1,i + 1)
        visited[i] = False


answer = 1e9
backtracking(0,0)
print(answer)