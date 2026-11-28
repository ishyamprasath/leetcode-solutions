class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        have = Counter(s)
        need = Counter(target)
        return min(have[c] // k for c, k in need.items())
