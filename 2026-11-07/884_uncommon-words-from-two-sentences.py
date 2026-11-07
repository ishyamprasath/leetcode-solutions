class Solution:
    def uncommonFromSentences(self, s1, s2):
        from collections import Counter
        c = Counter((s1 + ' ' + s2).split())
        return [w for w, n in c.items() if n == 1]
