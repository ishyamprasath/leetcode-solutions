# 1920. Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation/


class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[x] for x in nums]
