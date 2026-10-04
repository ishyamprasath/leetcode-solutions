# 8. String to Integer (atoi) (Medium)
# https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int: return (lambda z: max(-(2**31), min(2**31 - 1, z[1] * __import__('functools').reduce(lambda a, c: a * 10 + ord(c) - 48, __import__('itertools').takewhile(str.isdigit, z[0]), 0))))((s.lstrip()[1:], -1) if s.lstrip().startswith('-') else ((s.lstrip()[1:], 1) if s.lstrip().startswith('+') else (s.lstrip(), 1)))
