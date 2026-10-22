# 409. Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Use every pair of letters; one leftover letter can sit in the middle.
        length = 0
        has_odd = False
        for count in Counter(s).values():
            length += count // 2 * 2
            if count % 2 == 1:
                has_odd = True
        return length + 1 if has_odd else length
