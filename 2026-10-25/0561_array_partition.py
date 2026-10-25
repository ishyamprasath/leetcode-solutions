class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort, then pair neighbours; the smaller of each pair sits at even indices.
        nums.sort()
        return sum(nums[::2])
