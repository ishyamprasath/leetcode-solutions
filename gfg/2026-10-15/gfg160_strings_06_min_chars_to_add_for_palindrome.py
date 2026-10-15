# GFG 160 Strings 6: Min Chars to Add for Palindrome
# Prefix palindrome length via KMP LPS on s + '#' + reverse(s); answer is n - lps[-1].


class Solution:
    def minChar(self, s):
        n = len(s)
        temp = s + "#" + s[::-1]
        m = len(temp)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if temp[i] == temp[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        return n - lps[-1]
