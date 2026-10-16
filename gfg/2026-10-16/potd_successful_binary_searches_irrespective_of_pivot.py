# GFG POTD 2026-10-16: Successful Binary Searches Irrespective of Pivot
# Count indices always found under adversarial pivot binary search.
# Equivalent to: strictly greater than all on the left and strictly less than all on the right.


class Solution:
    def countAlwaysFound(self, arr):
        n = len(arr)
        pref_max = [0] * n
        pref_max[0] = arr[0]
        for i in range(1, n):
            pref_max[i] = max(pref_max[i - 1], arr[i])
        suf_min = [0] * n
        suf_min[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            suf_min[i] = min(suf_min[i + 1], arr[i])
        ans = 0
        for i in range(n):
            left_ok = i == 0 or pref_max[i - 1] < arr[i]
            right_ok = i == n - 1 or suf_min[i + 1] > arr[i]
            if left_ok and right_ok:
                ans += 1
        return ans
