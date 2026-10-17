# GFG 160 - Sorting 5: Insert Interval (Medium)


class Solution:
    def insertInterval(self, intervals, newInterval):
        result = []
        start, end = newInterval
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])
        while i < n:
            result.append(intervals[i])
            i += 1
        return result
