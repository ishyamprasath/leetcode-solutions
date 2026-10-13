# GFG 160 Arrays 9: Minimize the Heights
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/minimize-the-heights3351


class Solution:
    def getMinDiff(self, arr, k):
        a = sorted(arr)
        n = len(a)
        ans = a[-1] - a[0]
        for i in range(1, n):
            if a[i] - k < 0:
                continue
            mn = min(a[0] + k, a[i] - k)
            mx = max(a[i - 1] + k, a[-1] - k)
            ans = min(ans, mx - mn)
        return ans
