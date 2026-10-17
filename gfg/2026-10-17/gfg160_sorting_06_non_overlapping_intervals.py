# GFG 160 - Sorting 6: Non-Overlapping Intervals (Medium)


class Solution:
    def minRemoval(self, intervals):
        intervals.sort(key=lambda x: x[1])
        removed = 0
        last_end = float('-inf')
        for start, end in intervals:
            if start >= last_end:
                last_end = end
            else:
                removed += 1
        return removed
