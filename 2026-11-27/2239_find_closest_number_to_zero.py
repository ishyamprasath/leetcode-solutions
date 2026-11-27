class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # smallest distance to zero, ties broken by the larger value
        return min(nums, key=lambda x: (abs(x), -x))
