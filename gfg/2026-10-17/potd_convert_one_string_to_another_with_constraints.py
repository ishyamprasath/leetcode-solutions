# GFG POTD 2026-10-17: Convert One String to Another with Constraints (Easy)
# https://www.geeksforgeeks.org/problems/check-if-it-is-possible-to-convert-one-string-into-another-with-given-constraints4116/1


class Solution:
    def isItPossible(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        a = [(c, i) for i, c in enumerate(s1) if c != '#']
        b = [(c, i) for i, c in enumerate(s2) if c != '#']
        if len(a) != len(b):
            return False
        for (c1, i1), (c2, i2) in zip(a, b):
            if c1 != c2:
                return False
            if c1 == 'A' and i2 > i1:
                return False
            if c1 == 'B' and i2 < i1:
                return False
        return True
