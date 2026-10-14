# 1365. How Many Numbers Are Smaller Than the Current Number (Easy)
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        first_index = {}
        for i, x in enumerate(sorted(nums)):
            first_index.setdefault(x, i)
        return [first_index[x] for x in nums]
