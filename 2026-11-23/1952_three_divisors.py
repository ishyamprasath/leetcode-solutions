from typing import List
from collections import Counter
from math import gcd


class Solution:
    def isThree(self, n: int) -> bool:
        return sum(1 for d in range(1, n + 1) if n % d == 0) == 3
