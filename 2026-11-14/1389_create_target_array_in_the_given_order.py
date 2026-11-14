class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for value, pos in zip(nums, index):
            target.insert(pos, value)
        return target
