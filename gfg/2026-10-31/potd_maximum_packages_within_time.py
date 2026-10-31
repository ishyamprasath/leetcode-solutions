class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        n = len(arr)
        k = min(n, totalTime)
        window = sum(arr[:k])
        best = window
        for i in range(k, n):
            window += arr[i] - arr[i - k]
            best = max(best, window)
        return best
