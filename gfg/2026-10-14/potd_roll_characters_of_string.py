# GFG POTD 2026-10-14: Roll Characters of String
# https://www.geeksforgeeks.org/problems/roll-the-characters-of-a-string2127/1
# Each roll[i] shifts characters 0..roll[i]-1 by one. Mark +1 at index 0 and
# -1 at index roll[i] in a difference array; its prefix sum is the total shift
# for each position. O(n + m) time, O(n) space.


class Solution:
    def findRollOut(self, s, roll):
        n = len(s)
        diff = [0] * (n + 1)
        for r in roll:
            diff[0] += 1
            diff[r] -= 1
        out = []
        shift = 0
        for i, ch in enumerate(s):
            shift += diff[i]
            out.append(chr((ord(ch) - 97 + shift) % 26 + 97))
        return "".join(out)
