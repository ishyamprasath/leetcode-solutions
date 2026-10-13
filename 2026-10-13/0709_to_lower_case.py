# 709. To Lower Case
# https://leetcode.com/problems/to-lower-case/


class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in s)
