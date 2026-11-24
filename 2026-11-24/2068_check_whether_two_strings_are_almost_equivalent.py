from typing import List
from collections import Counter
from math import gcd


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        return all(abs(c1[ch] - c2[ch]) <= 3 for ch in "abcdefghijklmnopqrstuvwxyz")
