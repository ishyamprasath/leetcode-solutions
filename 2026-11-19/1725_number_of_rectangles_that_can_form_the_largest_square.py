class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        sides = [min(l, w) for l, w in rectangles]
        return sides.count(max(sides))
