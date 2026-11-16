from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        present = set(arr)
        x = 0
        while k > 0:
            x += 1
            if x not in present:
                k -= 1
        return x
