# 7. Reverse Integer (Medium)
# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int: return (lambda v: 0 if v > 2**31 - 1 else (-v if x < 0 else v))(int(str(abs(x))[::-1]))
