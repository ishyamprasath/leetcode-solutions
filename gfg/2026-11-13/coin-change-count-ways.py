class Solution:
    def count(self, coins: list[int], sum: int) -> int:
        ways = [0] * (sum + 1)
        ways[0] = 1
        for coin in coins:
            for s in range(coin, sum + 1):
                ways[s] += ways[s - coin]
        return ways[sum]
