# Duplicate Zeros — Easy — https://leetcode.com/problems/duplicate-zeros/
from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        expanded = []
        for value in arr:
            expanded.append(value)
            if value == 0:
                expanded.append(0)
        arr[:] = expanded[:len(arr)]
