from typing import List
from collections import Counter
import heapq

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)
        # find the first letter strictly greater than target
        while left < right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        # wrap around if no letter is greater
        return letters[left % len(letters)]
