class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nxt = []
            for i in range(len(nums) // 2):
                a, b = nums[2 * i], nums[2 * i + 1]
                nxt.append(min(a, b) if i % 2 == 0 else max(a, b))
            nums = nxt
        return nums[0]
