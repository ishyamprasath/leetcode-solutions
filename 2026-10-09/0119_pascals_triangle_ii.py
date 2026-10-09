# 119. Pascal's Triangle II (Easy)
# https://leetcode.com/problems/pascals-triangle-ii/
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            next_row = [1] * (len(row) + 1)
            for j in range(1, len(row)):
                next_row[j] = row[j - 1] + row[j]
            row = next_row
        return row
