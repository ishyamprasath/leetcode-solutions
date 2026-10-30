from typing import List
from collections import Counter
import heapq

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num: int) -> bool:
            n = num
            while n:
                digit = n % 10
                if digit == 0 or num % digit != 0:
                    return False
                n //= 10
            return True

        return [num for num in range(left, right + 1) if is_self_dividing(num)]
