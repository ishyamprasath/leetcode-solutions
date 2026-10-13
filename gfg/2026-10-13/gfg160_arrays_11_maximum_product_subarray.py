# GFG 160 Arrays 11: Maximum Product Subarray
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/maximum-product-subarray3604


class Solution:
    def maxProduct(self, arr):
        mx = mn = res = arr[0]
        for x in arr[1:]:
            if x < 0:
                mx, mn = mn, mx
            mx = max(x, mx * x)
            mn = min(x, mn * x)
            res = max(res, mx)
        return res
