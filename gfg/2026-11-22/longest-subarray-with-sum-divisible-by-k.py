class Solution:
    def longestSubarrayDivK(self, arr, k):
        # Two prefixes with the same remainder bound a subarray whose sum is divisible by k.
        first_index = {0: -1}
        prefix = 0
        best = 0
        for i, x in enumerate(arr):
            prefix = (prefix + x) % k
            if prefix in first_index:
                best = max(best, i - first_index[prefix])
            else:
                first_index[prefix] = i
        return best
