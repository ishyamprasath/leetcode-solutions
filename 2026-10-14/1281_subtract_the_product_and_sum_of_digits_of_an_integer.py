# 1281. Subtract the Product and Sum of Digits of an Integer (Easy)


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, total = 1, 0
        while n:
            n, d = divmod(n, 10)
            product *= d
            total += d
        return product - total
