# 925. Long Pressed Name (Easy)
from itertools import groupby


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        a = [(ch, sum(1 for _ in group)) for ch, group in groupby(name)]
        b = [(ch, sum(1 for _ in group)) for ch, group in groupby(typed)]
        return len(a) == len(b) and all(x[0] == y[0] and x[1] <= y[1] for x, y in zip(a, b))
