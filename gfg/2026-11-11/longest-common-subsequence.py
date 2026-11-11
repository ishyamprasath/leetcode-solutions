class Solution:
    def lcs(self, s1, s2):
        prev = [0] * (len(s2) + 1)
        for ch in s1:
            cur = [0]
            for j, other in enumerate(s2, 1):
                if ch == other:
                    cur.append(prev[j - 1] + 1)
                else:
                    cur.append(max(prev[j], cur[-1]))
            prev = cur
        return prev[-1]
