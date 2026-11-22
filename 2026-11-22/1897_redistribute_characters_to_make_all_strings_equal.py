from typing import List
from collections import Counter


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = Counter("".join(words))
        return all(c % len(words) == 0 for c in counts.values())
