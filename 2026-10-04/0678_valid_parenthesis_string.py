# 678. Valid Parenthesis String
# Difficulty: Medium
# URL: https://leetcode.com/problems/valid-parenthesis-string/
# Note: Problem of the Day (POD) — 2026-10-04
#
# Approach: greedy balance range.
# Track the possible open-count interval [lo, hi] while scanning left→right.
# '(' raises both bounds; ')' lowers both; '*' can act as '(', ')' or empty.
# Invalid if hi goes negative; valid only if lo ends at 0.

class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = 0  # minimum possible unmatched '('
        hi = 0  # maximum possible unmatched '('
        for ch in s:
            if ch == '(':
                lo += 1
                hi += 1
            elif ch == ')':
                lo = max(lo - 1, 0)
                hi -= 1
            else:  # '*'
                lo = max(lo - 1, 0)  # treat as ')' or empty
                hi += 1              # treat as '('
            if hi < 0:
                return False
        return lo == 0
