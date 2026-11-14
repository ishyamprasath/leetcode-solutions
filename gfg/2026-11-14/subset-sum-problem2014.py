class Solution:
    def equalPartition(self, arr):
        total = sum(arr)
        if total % 2:
            return False
        target = total // 2
        # bit i of reachable is set if subset sum i is possible
        reachable = 1
        for x in arr:
            reachable |= reachable << x
        return bool((reachable >> target) & 1)
