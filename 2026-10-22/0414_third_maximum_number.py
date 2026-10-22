# 414. Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Third largest distinct value, or the maximum if there are fewer than three.
        distinct = sorted(set(nums), reverse=True)
        if len(distinct) >= 3:
            return distinct[2]
        return distinct[0]
