# Problem: Add to Array-Form of Integer
# URL: https://leetcode.com/problems/add-to-array-form-of-integer/
# Difficulty: Easy
class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        i = len(num) - 1
        result = []
        while i >= 0 or k:
            if i >= 0:
                k += num[i]
                i -= 1
            result.append(k % 10)
            k //= 10
        return result[::-1]
