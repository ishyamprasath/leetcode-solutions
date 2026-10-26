class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        best = 0
        for value, freq in counts.items():
            if value + 1 in counts:
                best = max(best, freq + counts[value + 1])
        return best
