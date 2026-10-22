# Palindrome with Replacement (GFG Problem of the Day, 2026-10-22)
# https://www.geeksforgeeks.org/problems/palindrome-with-minimum-sum--170648/1

class Solution:
    def minimumSum(self, s: str) -> int:
        n = len(s)
        t = list(s)
        # Mirror known characters so the string becomes a palindrome
        for i in range(n // 2):
            j = n - 1 - i
            if t[i] == '?':
                t[i] = t[j]
            elif t[j] == '?':
                t[j] = t[i]
            elif t[i] != t[j]:
                return -1
        # Only the first half matters; the cost is doubled by symmetry
        half = t[:(n + 1) // 2]
        known = [ord(c) for c in half if c != '?']
        total = 0
        for a, b in zip(known, known[1:]):
            total += abs(a - b)
        return 2 * total
