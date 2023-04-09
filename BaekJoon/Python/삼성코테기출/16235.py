from collections import defaultdict

N,M,K = map(int,input().split())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))

mat = [[5] * (N+1) for _ in range(N+1)]
dict = defaultdict(list)
for _ in range(M):
    x,y,z = map(int,input().split())
    dict[(x,y)].append(z) 

for v in dict.values(): # 나이 순 정렬
    v.sort()

dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,1,-1,1,-1,-1,1]


for _ in range(K):
    dead = defaultdict(list)
    for i in range(4):
        if i == 0: # 봄
            
            for k in dict.keys():
                
                temp = []
                for idx,age in enumerate(dict[k]):  
                    if mat[k[0]][k[1]] < age:
                        dead[k].append(dict[k][idx])
                    else:
                        mat[k[0]][k[1]] -= age
                        age += 1    
                        temp.append(age)
                dict[k] = temp
        elif i == 1: # 여름 
            for k in dict.keys():
                for age in dead[k]:
                    mat[k[0]][k[1]] += (age // 2)
        elif i == 2: # 가을
            
            temp = defaultdict(list)
            
            for k in dict.keys():
                for age in dict[k]:
                    if age % 5 == 0:
                        for d in range(8):
                            nx = k[0] + dx[d]
                            ny = k[1] + dy[d] 
                            if 1<=nx<N+1 and 1<=ny<N+1:
                                temp[(nx,ny)].append(1)
                                
            for t,v in temp.items():
                dict[t].extend(v)
                dict[t].sort()

        elif i == 3: # 겨울
            for x in range(len(A)):
                for y in range(len(A[x])):
                    mat[x+1][y+1] += A[x][y]
    
result = 0                    
for v in dict.values():
    result += len(v)
            
print(result)
            