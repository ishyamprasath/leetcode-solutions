# GFG Problem of the Day 2026-10-19: Count Indices That Escape Array


class Solution:
    def goodIndices(self, arr):
        n = len(arr)
        state = [0] * n  # 0 unvisited, 1 in path, 2 good, 3 bad
        for s in range(n):
            if state[s]:
                continue
            path = []
            i = s
            res = 3
            while True:
                if i < 0 or i >= n:
                    res = 2
                    break
                if state[i] == 1:
                    res = 3
                    break
                if state[i] in (2, 3):
                    res = state[i]
                    break
                state[i] = 1
                path.append(i)
                if arr[i] == 0:
                    res = 3
                    break
                i += arr[i]
            for j in path:
                state[j] = res
        return sum(1 for x in state if x == 2)
