class Solution:
    def maximumSubarray(self, arr: list[int]) -> int:
        NEG = float('-inf')
        best = NEG
        no_sq = 0
        sq = NEG
        for x in arr:
            new_sq = max(max(no_sq, 0) + x * x, sq + x)
            no_sq = max(no_sq, 0) + x
            sq = new_sq
            best = max(best, sq, no_sq)
        return best
