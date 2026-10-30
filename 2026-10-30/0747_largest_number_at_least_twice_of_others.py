from typing import List
from collections import Counter
import heapq

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_index = max(range(len(nums)), key=lambda i: nums[i])
        largest = nums[max_index]
        for i, value in enumerate(nums):
            if i != max_index and value * 2 > largest:
                return -1
        return max_index
