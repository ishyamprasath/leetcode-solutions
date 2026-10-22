# Longest Consecutive Subsequence (GFG 160 - Hashing)
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/longest-consecutive-subsequence2449

class Solution:
    def longestConsecutive(self, arr):
        # Start counting only from numbers that begin a run
        nums = set(arr)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                length = 1
                while x + length in nums:
                    length += 1
                best = max(best, length)
        return best
