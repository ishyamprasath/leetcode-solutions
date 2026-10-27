# 645. Set Mismatch
# https://leetcode.com/problems/set-mismatch/
# Difficulty: Easy
# Approach: duplicate = sum(nums)-sum(set); missing = n(n+1)/2 - sum(set).
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set(nums)
        dup = sum(nums) - sum(s)
        missing = n * (n + 1) // 2 - sum(s)
        return [dup, missing]
