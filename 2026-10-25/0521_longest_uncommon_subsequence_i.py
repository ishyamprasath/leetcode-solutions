class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # If the strings differ, the longer one is an uncommon subsequence.
        if a == b:
            return -1
        return max(len(a), len(b))
