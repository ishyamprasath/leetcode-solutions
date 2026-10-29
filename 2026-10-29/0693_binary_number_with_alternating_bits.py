# 693. Binary Number with Alternating Bits
# https://leetcode.com/problems/binary-number-with-alternating-bits/
# Difficulty: Easy
# Approach: x = n ^ (n >> 1) is all ones iff bits alternate.
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return x & (x + 1) == 0
