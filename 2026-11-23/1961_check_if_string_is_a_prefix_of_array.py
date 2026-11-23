from typing import List
from collections import Counter
from math import gcd


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        built = ""
        for word in words:
            built += word
            if built == s:
                return True
            if len(built) >= len(s):
                return False
        return False
