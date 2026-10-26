class Solution:
    def maxLen(self, arr):
        # Treat 0 as -1; equal counts means subarray sum is 0.
        first_seen = {0: -1}
        balance = 0
        best = 0
        for i, value in enumerate(arr):
            balance += 1 if value == 1 else -1
            if balance in first_seen:
                best = max(best, i - first_seen[balance])
            else:
                first_seen[balance] = i
        return best
