# 3723. Maximize Sum of Squares of Digits (POD 2026-10-14, Medium)
# Squares are convex, so packing the digit sum into as many 9s as possible
# maximizes the score. Remaining sum goes in one digit, then zeros.
# Sorting digits in descending order gives the largest such integer.


class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        nines, rest = divmod(sum, 9)
        digits = "9" * nines + (str(rest) if rest else "")
        return digits + "0" * (num - len(digits))
