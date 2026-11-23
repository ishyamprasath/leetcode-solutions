from typing import List
from collections import Counter
from math import gcd


class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        for ch in s:
            if len(result) >= 2 and result[-1] == ch and result[-2] == ch:
                continue
            result.append(ch)
        return "".join(result)
