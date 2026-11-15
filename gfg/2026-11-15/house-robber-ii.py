class Solution:
    def maxValue(self, arr):
        def rob(houses):
            take, skip = 0, 0
            for value in houses:
                take, skip = skip + value, max(take, skip)
            return max(take, skip)

        if len(arr) == 1:
            return arr[0]
        return max(rob(arr[:-1]), rob(arr[1:]))
