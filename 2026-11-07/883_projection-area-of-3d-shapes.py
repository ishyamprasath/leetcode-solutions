class Solution:
    def projectionArea(self, grid):
        n = len(grid)
        xy = sum(v > 0 for row in grid for v in row)
        xz = sum(max(row) for row in grid)
        yz = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        return xy + xz + yz
