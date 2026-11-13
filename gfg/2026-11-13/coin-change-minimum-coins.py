class Solution:
    def minCoins(self, coins: list[int], sum: int) -> int:
        INF = float("inf")
        best = [0] + [INF] * sum
        for coin in set(coins):
            if coin > sum:
                continue
            for s in range(coin, sum + 1):
                candidate = best[s - coin] + 1
                if candidate < best[s]:
                    best[s] = candidate
        return -1 if best[sum] == INF else best[sum]
