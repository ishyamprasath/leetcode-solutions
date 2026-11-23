from typing import List
from collections import Counter
from math import gcd


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(1 for p in patterns if p in word)
