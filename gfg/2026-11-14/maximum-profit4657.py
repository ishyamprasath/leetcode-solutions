class Solution:
    def maxProfit(self, prices, k):
        n = len(prices)
        if n < 2 or k == 0:
            return 0
        k = min(k, n // 2)
        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)
        for p in prices:
            for t in range(1, k + 1):
                buy[t] = max(buy[t], sell[t - 1] - p)
                sell[t] = max(sell[t], buy[t] + p)
        return max(sell)
