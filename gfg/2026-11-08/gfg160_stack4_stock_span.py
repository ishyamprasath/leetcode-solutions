# GFG 160 Stack 4 (Day 102): Stock Span Problem
class Solution:
    def calculateSpan(self, arr):
        spans = [0] * len(arr)
        stack = []
        for i, price in enumerate(arr):
            while stack and arr[stack[-1]] <= price:
                stack.pop()
            spans[i] = i + 1 if not stack else i - stack[-1]
            stack.append(i)
        return spans
