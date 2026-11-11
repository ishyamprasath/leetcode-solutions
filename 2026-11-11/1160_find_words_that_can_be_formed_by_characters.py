from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        available = Counter(chars)
        total = 0
        for word in words:
            if not (Counter(word) - available):
                total += len(word)
        return total
