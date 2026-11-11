class Solution:
    def longestPalindrome(self, s):
        best_start = 0
        best_len = 1
        n = len(s)
        for center in range(2 * n - 1):
            left = center // 2
            right = (center + 1) // 2
            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1
                if length > best_len:
                    best_start = left
                    best_len = length
                left -= 1
                right += 1
        return s[best_start:best_start + best_len]
