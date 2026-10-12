class Solution:
    def maxProfit(self, prices):
        # Track the lowest price seen so far and the best profit from selling today.
        min_price = float('inf')
        best = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > best:
                best = price - min_price
        return best
