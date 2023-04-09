from collections import deque
N,M,oil = map(int,input().split())

mat = [[-1 for _ in range(N)]]

for _ in range(N):
    mat.append([0] + list(map(int,input().split())))
r,c = map(int,input().split())

info = []
for _ in range(M):
    a1,b1,a2,b2 = map(int,input().split())
    info.append([a1,b1,a2,b2])


moved = [0] * (M+1)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y,flag): # 택시로부터 최단거리 구하기 
    visited = [[-1 for _ in range(N+1)] for _ in range(N+1)]
    queue = deque([(x,y)])
    visited[x][y] = 0
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 1<=nx<N+1 and 1<=ny<N+1 and visited[nx][ny] == -1:
                if mat[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))

    min_dist = 1e9
    candidate = []
    if flag == 0:
        for idx,i in enumerate(info):
            if moved[idx]:
                continue
            start_x,start_y,dest_x,dest_y = i
            if min_dist >= visited[start_x][start_y]:
                min_dist = visited[start_x][start_y]
                candidate.append((start_x,start_y,dest_x,dest_y,idx,min_dist))
    
    
        candidate = sorted(candidate, key = lambda x: (x[5],x[0],x[1]))
        
        return [candidate[0][0],candidate[0][1],candidate[0][2],candidate[0][3],candidate[0][4],min_dist]
    else:
        return visited
        



for _ in range(M):
    new_r,new_c,dest_r,dest_c,idx,person_dist = bfs(r,c,0)
    
    if person_dist == -1:
        print(-1)
        break
    if oil < person_dist:
        print(-1)
        break

    oil -= person_dist
    a = bfs(new_r,new_c,1)
    move_dist = a[dest_r][dest_c]
    
    if oil < move_dist:
        print(-1)
        break

    r,c = dest_r,dest_c
    oil -= move_dist 
    oil += move_dist * 2
    moved[idx] = 1
else:
    print(oil)