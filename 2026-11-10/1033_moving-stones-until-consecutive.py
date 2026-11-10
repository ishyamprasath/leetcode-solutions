# Moving Stones Until Consecutive — Easy — https://leetcode.com/problems/moving-stones-until-consecutive/
from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, y, z = sorted((a, b, c))
        max_moves = z - x - 2
        if z - x == 2:
            min_moves = 0
        elif y - x <= 2 or z - y <= 2:
            min_moves = 1
        else:
            min_moves = 2
        return [min_moves, max_moves]
