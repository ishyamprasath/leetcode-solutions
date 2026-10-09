# 1541. Minimum Insertions to Balance a Parentheses String (Medium) - Problem of the Day, 2026-10-09
# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed = 0  # right parens still required
        for ch in s:
            if ch == '(':
                if needed % 2 == 1:
                    insertions += 1
                    needed -= 1
                needed += 2
            else:
                needed -= 1
                if needed < 0:
                    insertions += 1
                    needed += 2
        return insertions + needed
