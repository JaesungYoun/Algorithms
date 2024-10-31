from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    
    # 제한사항에서 모든 좌표값은 1 이상 50 이하라고 했고 2배의 좌표를 그려야 하므로 102*102 크기의 2차원 배열 선언
    field = [[-1] * 102 for i in range(102)]
    
    # 직사각형 그리기
    for r in rectangle:
    	# 테두리가 겹쳐 의도하지 않은 최단거리를 배제하기 위해 모든 좌표값 2배해서 테두리 좌표들끼리 인접하지 않도록
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        # x1부터 x2, y1부터 y2까지 순회
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
            	# x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 테두리일 때 1로 채움
                elif field[i][j] != 0:
                    field[i][j] = 1
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[0] * 102 for _ in range(102)]
    def bfs(x,y,itemX,itemY):
        queue = deque([(x,y)])
        
        visited[x][y] = 1
        
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<102 and 0<=ny<102 and field[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
                    
        return (visited[itemX][itemY] - 1) // 2
            
    answer = bfs(2*characterX,2*characterY,2*itemX,2*itemY)
    
    
    
    return answer