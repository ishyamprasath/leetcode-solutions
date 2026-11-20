class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        best = cur = nums[0]
        for i in range(1, len(nums)):
            cur = cur + nums[i] if nums[i] > nums[i - 1] else nums[i]
            best = max(best, cur)
        return best
