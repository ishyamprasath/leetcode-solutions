class Solution:
    def minSquares(self, n, m):
        # Cut the largest possible squares repeatedly (Euclidean algorithm).
        count = 0
        while n > 0 and m > 0:
            if n < m:
                n, m = m, n
            count += n // m
            n %= m
        return count
