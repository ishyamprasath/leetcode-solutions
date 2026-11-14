from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        lucky = [v for v, c in counts.items() if v == c]
        return max(lucky) if lucky else -1
