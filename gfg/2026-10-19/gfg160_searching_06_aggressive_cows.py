# GFG 160 - Searching 6: Aggressive Cows


class Solution:
    def aggressiveCows(self, arr, k):
        arr = sorted(arr)
        n = len(arr)
        lo, hi, ans = 1, arr[-1] - arr[0], 0
        while lo <= hi:
            mid = (lo + hi) // 2
            cnt = 1
            last = arr[0]
            for i in range(1, n):
                if arr[i] - last >= mid:
                    cnt += 1
                    last = arr[i]
                    if cnt >= k:
                        break
            if cnt >= k:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
