# 38. Count and Say (Medium)
# https://leetcode.com/problems/count-and-say/
class Solution:
    def countAndSay(self, n: int) -> str: return __import__('functools').reduce(lambda s, _: "".join(str(len(list(g))) + ch for ch, g in __import__('itertools').groupby(s)), range(n - 1), "1")
