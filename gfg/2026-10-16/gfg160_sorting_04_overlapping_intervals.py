# GFG 160 Sorting 4: Overlapping Intervals
# Sort by start, then merge any interval that overlaps the current merged end.


class Solution:
    def mergeOverlap(self, arr):
        if not arr:
            return []
        arr.sort(key=lambda x: x[0])
        merged = [list(arr[0])]
        for start, end in arr[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged
