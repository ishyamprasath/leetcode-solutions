from collections import deque


class Solution:
    def countIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        seen = [[False] * cols for _ in range(rows)]
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 'L' or seen[i][j]:
                    continue
                islands += 1
                seen[i][j] = True
                queue = deque([(i, j)])
                while queue:
                    r, c = queue.popleft()
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 'L' and not seen[nr][nc]:
                                seen[nr][nc] = True
                                queue.append((nr, nc))
        return islands
