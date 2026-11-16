from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        run = 0
        for x in arr:
            run = run + 1 if x % 2 else 0
            if run == 3:
                return True
        return False
