from typing import List
from collections import Counter
from math import gcd


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        return [original[i * n:(i + 1) * n] for i in range(m)]
