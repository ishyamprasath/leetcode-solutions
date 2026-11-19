class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        best_index = -1
        best_distance = float('inf')
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                distance = abs(a - x) + abs(b - y)
                if distance < best_distance:
                    best_distance = distance
                    best_index = i
        return best_index
