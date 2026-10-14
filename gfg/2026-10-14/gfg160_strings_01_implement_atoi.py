# GFG 160 Strings 1: Implement Atoi
# Skip leading spaces, read an optional sign, then digits until a non-digit,
# clamping the result to the 32-bit signed range.


class Solution:
    def myAtoi(self, s):
        INT_MAX, INT_MIN = 2**31 - 1, -(2**31)
        i, n = 0, len(s)
        while i < n and s[i] == " ":
            i += 1
        sign = 1
        if i < n and s[i] in "+-":
            if s[i] == "-":
                sign = -1
            i += 1
        value = 0
        while i < n and s[i].isdigit():
            value = value * 10 + (ord(s[i]) - ord("0"))
            if sign * value >= INT_MAX:
                return INT_MAX
            if sign * value <= INT_MIN:
                return INT_MIN
            i += 1
        return sign * value
