class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # s is built from a repeated block iff it appears inside (s + s) minus its ends
        return s in (s + s)[1:-1]
