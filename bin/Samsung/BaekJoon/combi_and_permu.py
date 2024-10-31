def permutation(arr,k):

    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == k:
            print(chosen)
            return

        # 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)

    def combination(arr, r):
        # 1.
        arr = sorted(arr)
        used = [0 for _ in range(len(arr))]

        # 2.
        def generate(chosen):
            if len(chosen) == r:
                print(chosen)
                return

            # 3.
            start = arr.index(chosen[-1]) + 1 if chosen else 0
            for nxt in range(start, len(arr)):
                if used[nxt] == 0 and (nxt == 0 or arr[nxt - 1] != arr[nxt] or used[nxt - 1]):
                    chosen.append(arr[nxt])
                    used[nxt] = 1
                    generate(chosen)
                    chosen.pop()
                    used[nxt] = 0

        generate([])