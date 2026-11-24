from typing import List
from collections import Counter
from math import gcd


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = -1
        for token in s.split():
            if token.isdigit():
                value = int(token)
                if value <= prev:
                    return False
                prev = value
        return True
