class Solution:
    def findSplit(self, arr):
        total = sum(arr)
        n = len(arr)
        if total % 3 != 0:
            return [-1, -1]
        part = total // 3
        prefix = 0
        i = -1
        for idx in range(n):
            prefix += arr[idx]
            if i == -1 and prefix == part:
                i = idx
            elif i != -1 and prefix == 2 * part and idx < n - 1:
                # third part arr[idx+1..n-1] is non-empty and sums to part
                return [i, idx]
        return [-1, -1]
