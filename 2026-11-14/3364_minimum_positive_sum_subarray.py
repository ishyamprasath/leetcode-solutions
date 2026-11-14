class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        best = None
        for start in range(n):
            total = 0
            for end in range(start, min(n, start + r)):
                total += nums[end]
                length = end - start + 1
                if length >= l and total > 0:
                    if best is None or total < best:
                        best = total
        return best if best is not None else -1
