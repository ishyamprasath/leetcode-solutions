# GFG 160 Arrays 13: Smallest Positive Missing
# Cyclic placement: put every value v in 1..n at index v-1, then the
# first index whose value is wrong gives the answer. O(n) time, O(1) space.


class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        for i in range(n):
            while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                j = arr[i] - 1
                arr[i], arr[j] = arr[j], arr[i]
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
        return n + 1
