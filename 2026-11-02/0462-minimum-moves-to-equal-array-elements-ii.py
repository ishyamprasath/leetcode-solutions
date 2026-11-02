# LeetCode 462. Minimum Moves to Equal Array Elements II (POD 2026-11-02)
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        med = nums[len(nums) // 2]
        return sum(abs(x - med) for x in nums)
