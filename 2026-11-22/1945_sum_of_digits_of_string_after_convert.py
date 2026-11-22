from typing import List
from collections import Counter


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digits = "".join(str(ord(ch) - ord("a") + 1) for ch in s)
        for _ in range(k):
            digits = str(sum(int(d) for d in digits))
        return int(digits)
