# GFG 160 Stack 5 (Day 103): Histogram Max Rectangular Area
class Solution:
    def getMaxArea(self, arr):
        n = len(arr)
        stack = []
        max_area = 0
        for i in range(n + 1):
            height = arr[i] if i < n else 0
            while stack and arr[stack[-1]] > height:
                bar_height = arr[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, bar_height * width)
            stack.append(i)
        return max_area
