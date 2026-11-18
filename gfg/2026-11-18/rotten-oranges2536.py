from collections import deque


class Solution:
    def orangesRot(self, mat):
        rows, cols = len(mat), len(mat[0])
        grid = [row[:] for row in mat]
        queue = deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        time = 0
        while queue and fresh > 0:
            time += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        queue.append((ni, nj))

        return time if fresh == 0 else -1
