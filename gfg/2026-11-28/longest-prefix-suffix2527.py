class Solution:
    def getLPSLength(self, s):
        # KMP failure function: lps[i] = longest proper prefix of s[:i+1]
        # that is also a suffix of it
        n = len(s)
        lps = [0] * n
        length = 0
        i = 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length:
                length = lps[length - 1]
            else:
                i += 1
        return lps[-1] if n else 0
