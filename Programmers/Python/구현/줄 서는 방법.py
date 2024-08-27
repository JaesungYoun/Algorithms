import math


def solution(n, k):
    nums = [i for i in range(1, n + 1)]
    answer = []
    k -= 1

    while nums:
        a = k // math.factorial(n - 1)
        print(k, math.factorial(n - 1))
        answer.append(nums[a])
        del nums[a]

        k = k % math.factorial(n - 1)

        n -= 1

    return answer