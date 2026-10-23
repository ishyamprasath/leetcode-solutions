class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        present = set(nums)
        return [v for v in range(1, len(nums) + 1) if v not in present]
