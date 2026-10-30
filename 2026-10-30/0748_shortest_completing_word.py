from typing import List
from collections import Counter
import heapq

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        need = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        best = None
        for word in words:
            if best is not None and len(word) >= len(best):
                continue
            have = Counter(word)
            if all(have[ch] >= cnt for ch, cnt in need.items()):
                best = word
        return best
