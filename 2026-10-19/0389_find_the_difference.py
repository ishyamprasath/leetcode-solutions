# LeetCode 389. Find the Difference (Easy)


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = 0
        for ch in s + t:
            x ^= ord(ch)
        return chr(x)
