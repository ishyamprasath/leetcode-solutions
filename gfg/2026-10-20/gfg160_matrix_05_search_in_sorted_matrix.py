# GFG 160 Matrix 5: Search in Sorted Matrix
class Solution:
    def searchMatrix(self, mat, x):
        # The matrix behaves like one sorted array of n * m elements,
        # so binary search over the flattened index.
        n, m = len(mat), len(mat[0])
        low, high = 0, n * m - 1
        while low <= high:
            mid = (low + high) // 2
            value = mat[mid // m][mid % m]
            if value == x:
                return True
            if value < x:
                low = mid + 1
            else:
                high = mid - 1
        return False
