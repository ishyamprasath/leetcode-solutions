# 1480. Running Sum of 1d Array (Easy)
# https://leetcode.com/problems/running-sum-of-1d-array/
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out, total = [], 0
        for x in nums:
            total += x
            out.append(total)
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert s.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert s.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
    print("ok")
