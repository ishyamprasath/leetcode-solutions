class Solution:
    def subarraySum(self, arr, target):
        left = 0
        window_sum = 0
        for right in range(len(arr)):
            window_sum += arr[right]
            while window_sum > target and left <= right:
                window_sum -= arr[left]
                left += 1
            if window_sum == target and left <= right:
                return [left + 1, right + 1]
        return [-1]
