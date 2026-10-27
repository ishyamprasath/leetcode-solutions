# 680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/
# Difficulty: Easy
# Approach: two pointers; on first mismatch try skipping either side.
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_pal(l + 1, r) or is_pal(l, r - 1)
            l += 1
            r -= 1
        return True
