class Solution:
    def maxWater(self, arr):
        left, right = 0, len(arr) - 1
        best = 0
        while left < right:
            height = min(arr[left], arr[right])
            best = max(best, height * (right - left))
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        return best
