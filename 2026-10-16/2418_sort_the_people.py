# LeetCode 2418. Sort the People (Easy)
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        order = sorted(range(len(names)), key=lambda i: -heights[i])
        return [names[i] for i in order]
