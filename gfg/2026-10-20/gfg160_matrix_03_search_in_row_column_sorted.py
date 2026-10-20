# GFG 160 Matrix 3: Search in a Row-Column Sorted Matrix
class Solution:
    def matSearch(self, mat, x):
        # Staircase search starting from the top-right corner.
        # Move left if the value is too large, down if it is too small.
        n, m = len(mat), len(mat[0])
        row, col = 0, m - 1
        while row < n and col >= 0:
            if mat[row][col] == x:
                return True
            if mat[row][col] > x:
                col -= 1
            else:
                row += 1
        return False
