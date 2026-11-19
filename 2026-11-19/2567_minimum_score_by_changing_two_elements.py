class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # Changing two elements lets the low score become 0, so we only
        # minimise the high score by "removing" two values from the ends.
        nums.sort()
        return min(
            nums[-1] - nums[2],   # change the two smallest
            nums[-3] - nums[0],   # change the two largest
            nums[-2] - nums[1],   # change the smallest and the largest
        )
