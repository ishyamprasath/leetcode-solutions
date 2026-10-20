# GFG 160 Matrix 4: Search in Row-Wise Sorted Matrix
from bisect import bisect_left


class Solution:
    def searchRowMatrix(self, mat, x):
        # Each row is sorted, so binary search every row independently.
        for row in mat:
            idx = bisect_left(row, x)
            if idx < len(row) and row[idx] == x:
                return True
        return False
