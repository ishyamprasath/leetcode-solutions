class Solution:
    def findEquilibrium(self, arr):
        total = sum(arr)
        left_sum = 0
        for i, value in enumerate(arr):
            # right sum excludes the current index
            if left_sum == total - left_sum - value:
                return i
            left_sum += value
        return -1
