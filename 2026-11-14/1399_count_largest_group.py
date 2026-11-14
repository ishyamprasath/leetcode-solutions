from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = Counter(sum(map(int, str(i))) for i in range(1, n + 1))
        largest = max(groups.values())
        return sum(1 for size in groups.values() if size == largest)
