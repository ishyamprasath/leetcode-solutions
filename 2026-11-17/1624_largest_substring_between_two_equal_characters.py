class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        best = -1
        for i, ch in enumerate(s):
            if ch in first:
                best = max(best, i - first[ch] - 1)
            else:
                first[ch] = i
        return best
