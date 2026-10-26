class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        res = [1] * n
        # res[i] holds the product of everything to the left of i
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= arr[i]
        # multiply by the product of everything to the right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= arr[i]
        return res
