# GFG Problem of the Day 2026-10-18: Shortest Path From 1 To n


class Solution:
    def minimumStep(self, n):
        # Work backwards from n: either walk down to the nearest multiple
        # of 3 and divide by 3, or walk straight down to 1.
        if n == 1:
            return 0
        if n == 2:
            return 1
        return min(n - 1, n % 3 + 1 + self.minimumStep(n // 3))
