import sys

N = int(sys.stdin.readline())

nums = list(map(int,sys.stdin.readline().split()))


for i in range(N-1,0,-1):
    if nums[i] > nums[i-1]:
        for j in range(N-1,0,-1):
            if nums[i-1] < nums[j]:
                nums[i-1], nums[j] = nums[j], nums[i-1]
                nums = nums[:i] + sorted(nums[i:])
                print(*nums)
                exit()
            
print(-1)
                