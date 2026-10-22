# 434. Number of Segments in a String
# https://leetcode.com/problems/number-of-segments-in-a-string/
class Solution:
    def countSegments(self, s: str) -> int:
        # split() with no arguments drops extra spaces, leaving only the segments.
        return len(s.split())
