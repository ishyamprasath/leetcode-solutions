# Nth in Concatenated Decimal String
# https://www.geeksforgeeks.org/problems/nth-character-in-concatenated-decimal-string0245/1
class Solution:
    def nthCharacter(self, n):
        digits, count, start = 1, 9, 1
        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10
        num = start + (n - 1) // digits
        return str(num)[(n - 1) % digits]
