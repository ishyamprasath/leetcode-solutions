from typing import List
from collections import Counter
from math import gcd


class Solution:
    def minimumMoves(self, s: str) -> int:
        moves = 0
        i = 0
        while i < len(s):
            if s[i] == "X":
                moves += 1
                i += 3
            else:
                i += 1
        return moves
