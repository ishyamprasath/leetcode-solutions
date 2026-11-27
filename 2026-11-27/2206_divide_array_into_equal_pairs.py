class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(c % 2 == 0 for c in Counter(nums).values())
