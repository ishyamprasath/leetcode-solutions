from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        cleaned = ''.join(ch.lower() if ch.isalpha() else ' ' for ch in paragraph)
        counts = {}
        best_word = ''
        best_count = 0
        for word in cleaned.split():
            if word in banned_set:
                continue
            counts[word] = counts.get(word, 0) + 1
            if counts[word] > best_count:
                best_count = counts[word]
                best_word = word
        return best_word
