class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        common = min(need1, need2)
        total = common * min(costBoth, cost1 + cost2)
        total += (need1 - common) * min(costBoth, cost1)
        total += (need2 - common) * min(costBoth, cost2)
        return total
