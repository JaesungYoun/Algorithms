from itertools import permutations
import sys

N = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))
A.sort()

arr = list(permutations(A,N))
sum = 0


for i in range(len(arr)):
    temp = 0
    for j in range(N-1):
        temp += abs(arr[i][j] - arr[i][j+1])
    if sum < temp:
        sum = temp

print(sum)