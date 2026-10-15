# GFG 160 Strings 5: Search Pattern (KMP Algorithm)
# Build LPS for the pattern, then run KMP to collect every start index (0-based).


class Solution:
    def search(self, pat, txt):
        m, n = len(pat), len(txt)
        if m == 0 or m > n:
            return []

        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

        res = []
        i = j = 0
        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
                if j == m:
                    res.append(i - j)  # 0-based
                    j = lps[j - 1]
            elif j:
                j = lps[j - 1]
            else:
                i += 1
        return res
