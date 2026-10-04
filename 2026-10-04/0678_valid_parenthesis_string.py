# 678. Valid Parenthesis String (Medium) - Problem of the Day, 2026-10-04
# https://leetcode.com/problems/valid-parenthesis-string/
class Solution:
    def checkValidString(self, s: str) -> bool: return (lambda p: p[2] and p[0] == 0)(__import__('functools').reduce(lambda p, c: ((p[0] + 1, p[1] + 1, p[2] and p[1] + 1 >= 0) if c == '(' else ((max(0, p[0] - 1), p[1] - 1, p[2] and p[1] - 1 >= 0) if c == ')' else (max(0, p[0] - 1), p[1] + 1, p[2] and p[1] + 1 >= 0))), s, (0, 0, True)))
