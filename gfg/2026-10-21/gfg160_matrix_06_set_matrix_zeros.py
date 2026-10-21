# Set Matrix Zeros
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/set-matrix-zeroes
class Solution:
    def setMatrixZeroes(self, mat):
        n, m = len(mat), len(mat[0])
        rows = set()
        cols = set()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:
                    mat[i][j] = 0
