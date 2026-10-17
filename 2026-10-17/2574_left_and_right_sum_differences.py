from typing import List

# 2574. Left and Right Sum Differences (Easy)


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left = 0
        answer = []
        for num in nums:
            right = total - left - num
            answer.append(abs(left - right))
            left += num
        return answer
