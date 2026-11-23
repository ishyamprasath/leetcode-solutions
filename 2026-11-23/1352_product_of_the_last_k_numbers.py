from typing import List
from collections import Counter
from math import gcd


class ProductOfNumbers:

    def __init__(self):
        # prefix[i] = product of the numbers added since the last zero (prefix[0] = 1)
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]  # any window that includes a zero has product 0
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0  # the last k numbers include a zero
        return self.prefix[-1] // self.prefix[-1 - k]
