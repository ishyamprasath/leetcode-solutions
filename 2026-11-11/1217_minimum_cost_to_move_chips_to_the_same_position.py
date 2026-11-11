class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_count = sum(pos % 2 == 0 for pos in position)
        return min(even_count, len(position) - even_count)
