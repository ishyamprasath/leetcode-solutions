from collections import deque

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        old = image[sr][sc]
        if old == newColor:
            return image
        n, m = len(image), len(image[0])
        image[sr][sc] = newColor
        queue = deque([(sr, sc)])
        while queue:
            r, c = queue.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < n and 0 <= nc < m and image[nr][nc] == old:
                    image[nr][nc] = newColor
                    queue.append((nr, nc))
        return image
