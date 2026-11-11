class Solution:
    def checkWithinK(self, arr: list[int], k: int) -> bool:
        last = {}
        for i, value in enumerate(arr):
            if value in last and i - last[value] <= k:
                return True
            last[value] = i
        return False
