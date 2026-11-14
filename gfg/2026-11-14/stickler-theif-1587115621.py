class Solution:
    def findMaxSum(self, arr):
        take, skip = 0, 0
        for x in arr:
            take, skip = skip + x, max(take, skip)
        return max(take, skip)
