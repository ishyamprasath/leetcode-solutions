# 1816. Truncate Sentence (Easy)


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])
