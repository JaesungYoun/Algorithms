import sys
N = int(sys.stdin.readline())

result = []

for i in range(N):
    result.append(sys.stdin.readline().strip())

answer = 0


for i in range(N):
    friend = 0 
    for j in range(N):
        if i == j :
            continue
        if result[i][j] == 'Y':
            friend += 1
        elif result[i][j] == 'N':
            
            for k in range(N):
                if result[j][k] == 'Y' and result[i][k] == 'Y':
                    friend += 1
                    break

    answer = max(answer,friend)
        
print(answer)