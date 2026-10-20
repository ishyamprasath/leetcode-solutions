# GFG 160 Matrix 2: Rotate by 90 degree
class Solution:
    def rotateMatrix(self, mat):
        # Anti-clockwise rotation by 90 degrees in place:
        # transpose the matrix, then reverse the order of the rows.
        n = len(mat)
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        mat.reverse()
