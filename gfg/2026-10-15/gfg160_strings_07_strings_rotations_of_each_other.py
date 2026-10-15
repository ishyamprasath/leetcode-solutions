# GFG 160 Strings 7: Strings Rotations of Each Other
# s2 is a rotation of s1 iff same length and s2 is a substring of s1+s1.


class Solution:
    def areRotations(self, s1, s2):
        return len(s1) == len(s2) and s2 in (s1 + s1)
