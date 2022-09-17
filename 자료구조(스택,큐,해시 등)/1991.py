import sys

N = int(sys.stdin.readline())

tree = dict()

for _ in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left,right]

def preorder(v):
    if v != ".": # 자식이 있다면
        print(v, end="") # 루트 노드 출력
        preorder(tree[v][0]) # 재귀적으로 왼쪽 노드 탐색
        preorder(tree[v][1]) # 재귀적으로 오른쪽 노드 탐색


# 중위 순회
def inorder(v):
    if v != ".": # 자식이 있다면
        inorder(tree[v][0]) # 재귀적으로 왼쪽 노드 탐색
        print(v, end="") # 루트 노드 출력
        inorder(tree[v][1]) # 재귀적으로 오른쪽 노드 탐색


# 후위 순회
def postorder(v):
    if v != ".": # 자식이 있다면
        postorder(tree[v][0]) # 재귀적으로 왼쪽 노드 탐색
        postorder(tree[v][1]) # 재귀적으로 오른쪽 노드 탐색
        print(v, end="") # 루트 노드 출력
        
preorder('A')
print()
inorder('A')
print()
postorder('A')