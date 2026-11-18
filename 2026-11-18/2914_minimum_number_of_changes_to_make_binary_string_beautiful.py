class Solution:
    def minChanges(self, s: str) -> int:
        # Look at each fixed pair (0,1), (2,3), ...; a pair must be "00" or "11"
        changes = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                changes += 1
        return changes
