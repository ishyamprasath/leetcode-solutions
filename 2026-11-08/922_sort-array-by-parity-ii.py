# 922. Sort Array By Parity II (Easy)
class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        even = iter(x for x in nums if x % 2 == 0)
        odd = iter(x for x in nums if x % 2)
        return [next(even) if i % 2 == 0 else next(odd) for i in range(len(nums))]
