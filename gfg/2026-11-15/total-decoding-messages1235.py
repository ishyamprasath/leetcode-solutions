class Solution:
    def countWays(self, digits):
        n = len(digits)
        if n == 0 or digits[0] == '0':
            return 0
        prev2, prev1 = 1, 1  # ways for prefixes of length i-2 and i-1
        for i in range(1, n):
            current = 0
            if digits[i] != '0':
                current += prev1
            two = int(digits[i - 1:i + 1])
            if digits[i - 1] != '0' and 10 <= two <= 26:
                current += prev2
            prev2, prev1 = prev1, current
        return prev1
