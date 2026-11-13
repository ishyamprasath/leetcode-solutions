class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        reachable = 1  # bit s is set when sum s can be formed
        for x in arr:
            reachable |= reachable << x
        return bool((reachable >> sum) & 1)
