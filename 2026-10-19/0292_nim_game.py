# LeetCode 292. Nim Game (Easy)


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
