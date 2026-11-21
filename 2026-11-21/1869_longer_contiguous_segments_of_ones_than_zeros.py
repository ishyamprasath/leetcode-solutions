from typing import List


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest = {"0": 0, "1": 0}
        run = 0
        for i, ch in enumerate(s):
            run = run + 1 if i and s[i - 1] == ch else 1
            longest[ch] = max(longest[ch], run)
        return longest["1"] > longest["0"]
