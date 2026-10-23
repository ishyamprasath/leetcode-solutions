class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # k must be a submask of every misplaced element; AND of misplaced ones is the max
        ans = -1
        for i, x in enumerate(nums):
            if x != i:
                ans &= x
        return 0 if ans == -1 else ans
