class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ok = set(allowed)
        return sum(set(word) <= ok for word in words)
