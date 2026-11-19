from collections import Counter


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = Counter(sum(map(int, str(n))) for n in range(lowLimit, highLimit + 1))
        return max(boxes.values())
