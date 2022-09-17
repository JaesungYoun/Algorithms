import sys

N = int(sys.stdin.readline())

move_list = list(map(int,sys.stdin.readline().split()))

balloon_list = [i for i in range(1,N+1)]


pop_idx = 0
move = move_list.pop(pop_idx)
result = []
result.append(balloon_list.pop(pop_idx))

while balloon_list:
    if move < 0 :
        pop_idx = (pop_idx + move) % len(move_list)
    else:
        pop_idx = (pop_idx + (move - 1)) % len(move_list)
    move = move_list.pop(pop_idx)
    result.append(balloon_list.pop(pop_idx))
    
for i in result:
    print(i, end = ' ')