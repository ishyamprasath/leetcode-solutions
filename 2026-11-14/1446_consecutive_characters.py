class Solution:
    def maxPower(self, s: str) -> int:
        best = 1
        run = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                run += 1
                best = max(best, run)
            else:
                run = 1
        return best
