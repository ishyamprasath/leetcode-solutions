# 1672. Richest Customer Wealth (Easy)
# https://leetcode.com/problems/richest-customer-wealth/
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(row) for row in accounts)


if __name__ == "__main__":
    s = Solution()
    assert s.maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6
    assert s.maximumWealth([[1, 5], [7, 3], [3, 5]]) == 10
    assert s.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
    print("ok")
