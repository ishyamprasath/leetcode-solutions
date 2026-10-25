class Solution:
    def longestSubarray(self, arr, k):
        first_seen = {0: -1}  # prefix sum -> earliest index
        prefix = 0
        best = 0
        for i, value in enumerate(arr):
            prefix += value
            if prefix - k in first_seen:
                best = max(best, i - first_seen[prefix - k])
            if prefix not in first_seen:
                first_seen[prefix] = i
        return best
