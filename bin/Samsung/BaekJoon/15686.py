N,M = map(int,input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))

result = 1e9
house = []
chicken = []
arr = []

# 미리 집과,치킨집의 좌표를 넣는게 포인트!
for i in range(N):
    for j in range(N):
     if mat[i][j] == 1:
        house.append((i,j))
     elif mat[i][j] == 2:
        chicken.append((i,j))


def dfs(cnt,idx):
    global result

    if cnt == M:
        dist = 0
        for hx,hy in house:
            temp = 1e9
            for i in arr:
                cx,cy = chicken[i]
                temp = min(temp, abs(hx -cx) + abs(hy-cy))
            dist += temp
        result = min(result,dist)
        return

    for i in range(idx,len(chicken)):
        arr.append(i)
        dfs(cnt + 1,i+1)
        arr.pop()


dfs(0,0)

print(result)