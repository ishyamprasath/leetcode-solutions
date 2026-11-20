class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        prev = nums[0]
        for x in nums[1:]:
            need = max(x, prev + 1)
            ops += need - x
            prev = need
        return ops
