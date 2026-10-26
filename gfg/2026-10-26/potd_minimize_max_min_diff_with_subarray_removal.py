class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
        n = len(arr)
        INF = float('inf')
        # pmin[i], pmax[i]: min/max of arr[:i]
        pmin = [INF] * (n + 1)
        pmax = [-INF] * (n + 1)
        for i in range(n):
            pmin[i + 1] = min(pmin[i], arr[i])
            pmax[i + 1] = max(pmax[i], arr[i])
        # smin[i], smax[i]: min/max of arr[i:]
        smin = [INF] * (n + 1)
        smax = [-INF] * (n + 1)
        for i in range(n - 1, -1, -1):
            smin[i] = min(smin[i + 1], arr[i])
            smax[i] = max(smax[i + 1], arr[i])
        best = INF
        for i in range(n - k + 1):
            lo = min(pmin[i], smin[i + k])
            hi = max(pmax[i], smax[i + k])
            best = min(best, hi - lo)
        return best
