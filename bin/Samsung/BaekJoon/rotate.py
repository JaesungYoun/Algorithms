def rotate_90(m):
    N = len(m)
    ret = [[0 for _ in range(N)] for _ in range(N)]
    # 왜 'ret = [[0] * N] * N'과 같이 하지 않는지 헷갈리시면 연락주세요.

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

test = [[1,2,3], [4,5,6], [7,8,9]]
print(rotate_90(test))


def rotate_180(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-r][N-1-c] = m[r][c]
    return ret


test = [[1,2,3], [4,5,6], [7,8,9]]
print(rotate_180(test))


def rotate_270(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)] # 새로운 배열에 담아놓음

    for r in range(N):
        for c in range(N):
            ret[N-1-c][r] = m[r][c]
    return ret


test = [[1,2,3], [4,5,6], [7,8,9]]
print(rotate_270(test))

arr = [[1,2,3],[4,5,6],[7,8,9]]

# 반시계
temp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
for i in range(len(arr)):
    for j in range(len(arr)):
        temp[i][j] = arr[j][len(arr) - 1 - i]

print("반시계 90도",temp)
## 시계
for i in range(len(arr)):
    for j in range(len(arr)):
        temp[i][j] = arr[len(temp) - 1 - j][i]

print("시계 90도",temp)


'''
move = [[0,1],[1,0],[0,-1],[-1,0]]
direction = 0

if commands == 'L': # command 가 L 이면 반시계방향 회전
direction = (direction - 1) % 4
elif commands == 'D': # command 가 D 이면 시계방향 회전
direction = (direction + 1) % 4
'''